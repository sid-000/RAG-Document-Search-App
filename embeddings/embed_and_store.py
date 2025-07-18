
import os
import pickle
import faiss
from typing import List, Dict
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

# Load model (you can replace with 'all-MiniLM-L6-v2' or your favorite)
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings(texts: List[str]) -> List[List[float]]:
    return model.encode(texts, show_progress_bar=True)


def build_faiss_index(chunks: List[Dict], save_dir: str = "embeddings/faiss_store"):
    os.makedirs(save_dir, exist_ok=True)

    # Extract just the text
    texts = [chunk["text"] for chunk in chunks]
    metadata = [
    {
        "source": chunk["source"],
        "chunk_index": chunk["chunk_index"],
        "text": chunk["text"]
    }
    for chunk in chunks]


    # Get embeddings
    print("Generating embeddings...")
    vectors = get_embeddings(texts)

    # Create FAISS index
    dim = len(vectors[0])
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

    # Save index + metadata
    faiss.write_index(index, os.path.join(save_dir, "index.faiss"))
    with open(os.path.join(save_dir, "metadata.pkl"), "wb") as f:
        pickle.dump(metadata, f)

    print(f"Saved FAISS index and metadata for {len(chunks)} chunks.")
