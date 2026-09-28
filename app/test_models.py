from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import GOOGLE_API_KEY, GROQ_API_KEY


def test_groq():
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        groq_api_key=GROQ_API_KEY,
    )

    response = llm.invoke("Explain RAG in one sentence.")

    print("\nGroq response:")
    print(response.content)


def test_gemini_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=GOOGLE_API_KEY,
    )

    vector = embeddings.embed_query("What is RAG?")

    print("\nEmbedding information:")
    print("Type:", type(vector))
    print("Dimensions:", len(vector))
    print("First 5 values:", vector[:5])


if __name__ == "__main__":
    test_groq()
    test_gemini_embeddings()