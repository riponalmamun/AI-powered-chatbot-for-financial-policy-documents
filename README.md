# 📘 AI-Powered Chatbot for Document Question Answering
# 📖 Introduction

This project is an AI-powered chatbot that can answer questions from documents, such as financial policy reports. The chatbot extracts key information from PDFs, stores it in a vector database, and retrieves the most relevant sections to answer user queries. It also includes conversation memory, allowing follow-up questions to stay in context.

The main goal is to demonstrate how AI can combine document retrieval with natural language processing to provide clear, context-aware responses.

# ⚙️ How It Works

1. **Extract Data –** The document (PDF) is parsed and split into smaller sections. Each section is stored with metadata (page number/section).

2. **Embed & Store –** Text sections are converted into embeddings using a pre-trained model and stored in a vector database (FAISS/ChromaDB).

3. **User Query –** When a user asks a question, the chatbot embeds the query and searches for the most relevant document sections.

4. **Answer Generation –** The retrieved section(s) are used to generate a clear and helpful response.

5. **Conversation Memory –** Previous queries are stored so the chatbot can understand follow-up questions (e.g., “What about debt?” after a budget question).


# 📦 Dependencies and Installation
Requirements
🌟 Dependencies

**Python 3.10+

Streamlit

LangChain

FAISS

PyPDF2

Transformers

python-dotenv**

**Libraries:**
pip install langchain sentence-transformers faiss-cpu chromadb pdfplumber


📖 References

LangChain Documentation
