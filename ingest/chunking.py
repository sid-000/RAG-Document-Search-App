from typing import List, Dict


def chunk_text(text: str, chunk_size: int = 500) -> List[str]:
    paragraphs = text.split("\n\n")
    chunks = []

    current_chunk = ""
    for para in paragraphs:
        if len(current_chunk.split()) + len(para.split()) < chunk_size:
            current_chunk += " " + para.strip()
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para.strip()

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks



def create_chunks(documents: List[tuple], chunk_size: int = 500) -> List[Dict]:
    """
    Creates chunks from list of documents.

    Args:
        documents: List of (filename, text)
        chunk_size: Number of words per chunk

    Returns:
        List of dicts with keys: 'source', 'chunk_index', 'text'
    """
    all_chunks = []

    for filename, text in documents:
        chunks = chunk_text(text, chunk_size)
        for idx, chunk in enumerate(chunks):
            all_chunks.append({
                "source": filename,
                "chunk_index": idx,
                "text": chunk
            })

    return all_chunks
