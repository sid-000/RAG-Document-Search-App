from retriever.retrieve import search_faiss
from llm.generate import ask_llm
import tiktoken

def truncate_to_token_limit(text: str, model: str = "gpt-3.5-turbo", max_tokens: int = 3000) -> str:
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)
    truncated = tokens[:max_tokens]
    return enc.decode(truncated)


if __name__ == "__main__":
    question = "What are transformers used for in NLP?"
    top_chunks = search_faiss(question, top_k=4)

    if not top_chunks:
        print("No chunks found.")
    else:
        context = "\n\n".join([chunk for (_, _, chunk) in top_chunks])
        truncated_context = truncate_to_token_limit(context, max_tokens=3000)
        answer = ask_llm(truncated_context, question)


        print("Question:", question)
        print("\n Retrieved Context:", context)
        print("\n Answer:\n", answer)
# pipeline integration test 
