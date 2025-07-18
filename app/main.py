import streamlit as st
from retriever.retrieve import search_faiss
from llm.generate import ask_llm

st.set_page_config(page_title="RAG Document Search", layout="wide")
st.title("RAG-Powered Document Q&A")

question = st.text_input("💬 Ask a question based on the uploaded documents:", "")

if st.button("Search") and question:
    with st.spinner("Retrieving context..."):
        top_chunks = search_faiss(question, top_k=4)

    if not top_chunks:
        st.warning("No relevant chunks found.")
    else:
        context = "\n\n".join([chunk for (_, _, chunk) in top_chunks])

        st.subheader("Retrieved Context")
        st.text_area("Chunks Used for Answering", context, height=200)

        with st.spinner("Generating answer..."):
            try:
                import tiktoken
                def truncate_to_token_limit(text: str, model: str = "gpt-3.5-turbo", max_tokens: int = 3000) -> str:
                    enc = tiktoken.encoding_for_model(model)
                    tokens = enc.encode(text)
                    truncated = tokens[:max_tokens]
                    return enc.decode(truncated)

                truncated_context = truncate_to_token_limit(context)
                answer = ask_llm(truncated_context, question)
                st.success("Done!")
                st.subheader("Answer")
                st.markdown(answer)
            except Exception as e:
                st.error(f"Failed to get answer: {e}")
