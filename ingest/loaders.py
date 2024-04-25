import os
import fitz  # PyMuPDF
from typing import List, Tuple


def load_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf(file_path: str) -> str:
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


def load_documents(data_dir: str = "data") -> List[Tuple[str, str]]:
    """
    Loads .pdf and .txt files from the data directory.

    Returns:
        List of tuples: (filename, text_content)
    """
    documents = []

    for filename in os.listdir(data_dir):
        file_path = os.path.join(data_dir, filename)

        if filename.endswith(".txt"):
            text = load_txt(file_path)
        elif filename.endswith(".pdf"):
            text = load_pdf(file_path)
        else:
            continue

        documents.append((filename, text))

    return documents
# added PDF loader 
