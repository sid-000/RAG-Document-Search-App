import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def format_prompt(context: str, question: str) -> str:
    return f"""You are an intelligent assistant. Use the context below to answer the question.

Context:
{context}

Question:
{question}

Answer:"""


def ask_llm(context: str, question: str, model: str = "gpt-3.5-turbo") -> str:
    prompt = format_prompt(context, question)

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=500
    )

    return response['choices'][0]['message']['content'].strip()
# generate response from query 
