# 🧠 RAG Document Search App

A full-stack **Retrieval-Augmented Generation (RAG)** pipeline that ingests documents (PDFs, TXT), indexes them into a vector store, and allows users to query those documents through a language model-powered interface.

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




## 🧪 Sample Q&A Results

**Document:** `NLP_intro.pdf`  
**Question:** What are transformers used for in NLP?  
**Retrieved Context Snippet:**  
> Transformers are used in NLP for tasks such as translation, summarization, and question answering...

**Answer:**  
Transformers are used in NLP for tasks like translation, summarization, and QA by modeling long-range dependencies using self-attention mechanisms.

---

**Document:** `transformers_overview.pdf`  
**Question:** Who introduced the transformer model?  
**Answer:**  
The Transformer model was introduced in the paper *"Attention is All You Need"* by Vaswani et al., 2017.




## 📄 Sample Documents

The RAG system was tested on real-world NLP-related PDFs:

- [Attention Is All You Need (Vaswani et al., 2017)](data/Attention_Is_All_You_Need.pdf)
- [Natural Language Processing: A Comprehensive Survey](data/NLP_Comprehensive_Survey.pdf)

These documents were embedded using `sentence-transformers`, stored using `FAISS`, and queried with natural language questions.



