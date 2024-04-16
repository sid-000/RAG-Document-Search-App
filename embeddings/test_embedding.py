from ingest.loaders import load_documents
from ingest.chunking import create_chunks
from embeddings.embed_and_store import build_faiss_index

if __name__ == "__main__":
    docs = load_documents("data")
    chunks = create_chunks(docs, chunk_size=500)
    build_faiss_index(chunks)
# testing embedding accuracy 
