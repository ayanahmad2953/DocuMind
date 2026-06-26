# 📄 DocuMind - AI Powered PDF Question Answering System

An AI-powered PDF Question Answering application that enables users to upload PDF documents and ask questions in natural language using Retrieval-Augmented Generation (RAG), FAISS, LangChain, and Hugging Face Transformers.

---

## 🚀 Live Demo

🌐 **Live Website:** https://ayanahmad2953-documind.hf.space

🤗 **Hugging Face Space:** https://huggingface.co/spaces/ayanahmad2953/DocuMind

💻 **GitHub Repository:** https://github.com/ayanahmad2953/DocuMind

---

## ✨ Features

- 📄 Upload any PDF document
- 🤖 Ask questions in natural language
- 🔍 Semantic search using FAISS Vector Database
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Fast document retrieval with Sentence Transformers
- 💬 AI-generated answers grounded in uploaded PDF content
- 🌐 Interactive Gradio interface
- 🔒 Processes one uploaded document at a time

---

## 🛠️ Tech Stack

- Python
- Gradio
- LangChain
- FAISS
- Hugging Face Transformers
- Sentence Transformers
- PyPDF
- Recursive Character Text Splitter

---

## 📂 Project Structure

```text
DocuMind/
│
├── app.py
├── rag.py
├── llm.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/ayanahmad2953/DocuMind.git
cd DocuMind
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 🧠 How It Works

1. Upload a PDF document.
2. Extract text using PyPDFLoader.
3. Split text into chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in FAISS.
6. Retrieve the most relevant chunks for the user's question.
7. Generate an answer using a Hugging Face language model.

---

## 📌 Future Improvements

- OCR support for scanned PDFs
- Multi-PDF chat
- Conversation history
- Source citations
- PDF summarization
- Support for larger documents

---

## 👨‍💻 Author

**Ayan Ahmad**

GitHub: https://github.com/ayanahmad2953

---

## ⭐ If you found this project useful, please consider giving it a star!
