# 📘 AI-Powered Chatbot for Document Question Answering
# 📖 Introduction

This project is an AI-powered chatbot that can answer questions from documents, such as financial policy reports. The chatbot extracts key information from PDFs, stores it in a vector database, and retrieves the most relevant sections to answer user queries. It also includes conversation memory, allowing follow-up questions to stay in context.

The main goal is to demonstrate how AI can combine document retrieval with natural language processing to provide clear, context-aware responses.

# 🚀 Features

1. Conversational chatbot for financial policy queries

2. Built using Python + Streamlit

3. Easy to deploy locally or on cloud platforms

4. Customizable Q&A system


# ⚙️ How It Works

1. **Extract Data –** The document (PDF) is parsed and split into smaller sections. Each section is stored with metadata (page number/section).

2. **Embed & Store –** Text sections are converted into embeddings using a pre-trained model and stored in a vector database (FAISS/ChromaDB).

3. **User Query –** When a user asks a question, the chatbot embeds the query and searches for the most relevant document sections.

4. **Answer Generation –** The retrieved section(s) are used to generate a clear and helpful response.

5. **Conversation Memory –** Previous queries are stored so the chatbot can understand follow-up questions (e.g., “What about debt?” after a budget question).


# 🛠️ Project Structure

├── **app.py**                 # Main Streamlit application

├── **requirements.txt**      # List of dependencies

├── **.env**                  # Environment variables (API keys, configs)

├── **README.md**              # Project documentation


# 📦 Dependencies and Installation
Requirements : 

Python 3.9+

pip package manager

# Setup

1️⃣ Clone the Repository

Clone the repository from GitHub
```bash
git clone https://github.com/your-username/financial-policy-chatbot.git
```

Change into the project folder
```bash
cd financial-policy-chatbot
```
2️⃣ Create Virtual Environment
Create a virtual environment named 'venv'
```bash
python -m venv venv
```
Activate the environment (Mac/Linux)
```bash
source venv/bin/activate
```
Activate the environment (Windows)
```bash
venv\Scripts\activate
```
3️⃣ Install Dependencies
Install all required Python dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Configure Environment Variables

Create a .env file in the project root and add your API key:
```bash
OPENAI_API_KEY=your_api_key_here
```
▶️ Running the App
Run the Streamlit app locally
```bash
streamlit run app.py
```

Then open your browser at:
```bash
👉 http://localhost:8501
```
# 🧪 Example Questions

What are the financial policy objectives of the government?

Explain the difference between fiscal and monetary policy.

What strategies can improve financial transparency?

# 🔧 Troubleshooting

Error: NoneType object is not callable
→ Ensure you are calling the conversation chain correctly in handle_userinput.

Port conflict (8501 already in use)
→ Run with a custom port:

streamlit run app.py --server.port 8502

# 🤝 Contributing

Contributions are welcome! Please fork the repository, make your changes, and create a pull request.


## 📸 Project Screenshots

Here are some screenshots showing the output of the Financial Policy Chatbot:

<img width="1918" height="907" alt="image" src="https://github.com/user-attachments/assets/64995311-41e1-46ac-9c8a-58c06dd6655e" />

<img width="1910" height="905" alt="image" src="https://github.com/user-attachments/assets/0ae53c48-835b-44c5-9633-336c598b021f" />

**Note:** Screenshots demonstrate the chatbot interface and functionality.






