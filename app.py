import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS  # Updated import
from langchain_community.llms import HuggingFacePipeline  # Updated import
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from htmlTemplates import css, bot_template, user_template

# ---------------- PDF Processing ----------------
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(text)

# ---------------- Vector Store ----------------
def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

# ---------------- LLM & Conversation Chain ----------------
def get_conversation_chain(vectorstore):
    model_name = "google/flan-t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=512,
        temperature=0.3
    )

    llm = HuggingFacePipeline(pipeline=pipe)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# ---------------- Handle User Input ----------------
def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.warning("Please upload and process at least one PDF first.")
        return

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

# ---------------- Main App ----------------
def main():
    load_dotenv()
    st.set_page_config(
        page_title="FINANCIAL POLICY OBJECTIVES AND STRATEGIES STATEMENT",
        page_icon=":books:"
    )
    st.write(css, unsafe_allow_html=True)

    # Initialize session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("FINANCIAL POLICY OBJECTIVES AND STRATEGIES STATEMENT :books:")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True
        )

        if pdf_docs:
            st.write("Uploaded files:")
            for pdf in pdf_docs:
                st.write(pdf.name)

        if st.button("Process"):
            if pdf_docs:
                with st.spinner("Processing PDFs..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vectorstore = get_vectorstore(text_chunks)
                    st.session_state.conversation = get_conversation_chain(vectorstore)
                    st.success("PDFs processed! You can now ask questions.")
            else:
                st.warning("Please upload at least one PDF.")

    # Only show input after PDFs are processed
    if st.session_state.conversation is not None:
        user_question = st.text_input("Ask a question about your documents:")
        if user_question:
            handle_userinput(user_question)
    else:
        st.info("Upload and process your PDFs first to start asking questions.")

if __name__ == '__main__':
    main()
