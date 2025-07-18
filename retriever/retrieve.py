import faiss
import pickle
import numpy as np
from typing import List, Tuple
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_faiss_index(index_path: str, metadata_path: str):
    index = faiss.read_index(index_path)
    with open(metadata_path, "rb") as f:
        metadata = pickle.load(f)
    return index, metadata


def embed_query(query: str) -> np.ndarray:
    return model.encode([query])[0]


def search_faiss(query: str,
                 index_path: str = "embeddings/faiss_store/index.faiss",
                 metadata_path: str = "embeddings/faiss_store/metadata.pkl",
                 top_k: int = 5) -> List[Tuple[str, int, str]]:
    """
    Searches for top_k similar chunks for a given query.

    Returns:
        List of (source, chunk_index, text)
    """
    index, metadata = load_faiss_index(index_path, metadata_path)
    query_vector = embed_query(query)

    distances, indices = index.search(np.array([query_vector]), top_k)
    results = []

    for idx in indices[0]:
        if idx < len(metadata):
            meta = metadata[idx]
            results.append((meta["source"], meta["chunk_index"], meta.get("text", "")))

    return results
