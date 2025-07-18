# 🧠 RAG Document Search App

A full-stack **Retrieval-Augmented Generation (RAG)** pipeline that ingests documents (PDFs, TXT), indexes them into a vector store, and allows users to query those documents through a language model-powered interface.

---


🗓️ Project Timeline

Originally Started: March 2024

Finalized: May 2024

Portfolio Update: July 2025

---


## 🔹 Demo

Here’s a quick walkthrough of the app in action:

![Demo](assets/demo.gif)

---


## 🚀 Features

- 📥 Upload `.pdf` and `.txt` files from your local system
- ✂️ Automatic document chunking
- 🔍 Embedding with `sentence-transformers` or OpenAI
- 🧠 Vector storage using `FAISS`
- 🤖 OpenAI GPT-3.5 or GPT-4 powered Q&A
- 🌐 Simple UI with Streamlit

---

## 🛠️ Tech Stack

| Component         | Tool                         |
|------------------|------------------------------|
| Chunking         | Custom, via word splitter    |
| Embeddings       | `sentence-transformers` / OpenAI |
| Vector DB        | `FAISS`                      |
| LLM Inference    | `OpenAI GPT-3.5` / `GPT-4`   |
| Frontend         | `Streamlit`                  |
| PDF Parsing      | `PyMuPDF`                    |
| API Key Handling | `python-dotenv`              |

---

## 📁 Folder Structure

```bash
rag-document-search-app/
├── data/                      # Raw documents (PDFs, TXTs)
├── ingest/                    # Loading and chunking logic
│   ├── __init__.py
│   ├── loaders.py
│   └── chunking.py
├── embeddings/                # Embedding generation and vector store
│   ├── __init__.py
│   └── embed_and_store.py
├── retriever/                 # Query handling and retrieval
│   ├── __init__.py
│   └── retrieve.py
├── llm/                       # Prompt formatting and LLM response
│   ├── __init__.py
│   └── generate.py
├── app/                       # Streamlit frontend
│   ├── __init__.py
│   └── main.py
├── requirements.txt
├── README.md
└── .env                       # Contains your OpenAI API key



---

## 🔧 Setup Instructions

1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/Deep-Learning---Project-1.git
cd Deep-Learning---Project-1


2. Install dependencies

pip install -r requirements.txt


3. Add your OpenAI key in .env:

OPENAI_API_KEY=sk-xxxxxxxxxxxx


4. Run the app

streamlit run app/main.py


---

📘 Sample Q&A Results
Below are sample interactions demonstrating how the app extracts answers based on uploaded documents.

📄 Source: "Attention Is All You Need"
Q: What are transformers used for in NLP?
A:
Transformers are deep learning models that rely entirely on self-attention mechanisms, removing the need for recurrence. In NLP, they are used for tasks like machine translation, summarization, and question answering. Their parallelizable structure significantly improves training efficiency and accuracy across sequence modeling tasks.

Q: What is self-attention?
A:
Self-attention is a mechanism that allows a model to weigh the importance of different words in a sentence relative to each other. It computes representations of input tokens by attending to all positions in the sequence, enabling the model to capture contextual relationships more effectively.

📄 Source: "A Comprehensive Survey of NLP"
Q: What are the major tasks in NLP covered in the survey?
A:
The survey covers a wide range of NLP tasks including part-of-speech tagging, named entity recognition, machine translation, sentiment analysis, question answering, and text summarization. It also explores emerging areas like emotion detection and multilingual modeling.

Q: What are some challenges in current NLP research?
A:
Key challenges include handling ambiguity in language, bias in training data, scalability of models, data sparsity in low-resource languages, and ensuring interpretability of deep models like transformers.


---

## 📄 Sample Documents

The RAG system was tested on real-world NLP-related PDFs:

- [Attention Is All You Need (Vaswani et al., 2017)](data/Attention_Is_All_You_Need.pdf)
- [Natural Language Processing: A Comprehensive Survey](data/NLP_Comprehensive_Survey.pdf)

These documents were embedded using `sentence-transformers`, stored using `FAISS`, and queried with natural language questions.


