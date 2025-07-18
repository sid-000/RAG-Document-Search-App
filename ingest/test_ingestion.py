from loaders import load_documents
from chunking import create_chunks

if __name__ == "__main__":
    docs = load_documents("data")
    print(f"Loaded {len(docs)} documents")

    chunks = create_chunks(docs, chunk_size=500)
    print(f"Generated {len(chunks)} chunks")
    print("Sample chunk:\n", chunks[0] if chunks else "No chunks found.")
