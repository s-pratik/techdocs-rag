from functools import lru_cache

from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY
from app.context import build_context
from app.prompt import RAG_PROMPT
from app.retriever import hybrid_search

@lru_cache(maxsize=1)
def get_llm():
    return ChatGroq(
        model="openai/gpt-oss-20b",
        groq_api_key=GROQ_API_KEY,
        temperature=0,
        max_retries=2,
    )


def answer_question(question: str):
    results = hybrid_search(question, k=3)

    if not results:
        return {
            "answer": (
                "I don't have enough information in the provided "
                "documents to answer that question."
            ),
            "sources": [],
            "context_tokens": 0,
        }

    context, context_tokens = build_context(results)

    llm = get_llm()

    chain = RAG_PROMPT | llm | StrOutputParser()

    answer = chain.invoke(
        {
            "context": context,
            "question": question,
        },
        config={
            "tags": ["rag", "techdocs"],
            "metadata": {
                "retrieval_k": 3,
                "context_tokens": context_tokens,
            },
        },
    )

    sources = [
        {
            "source": document.metadata.get("source"),
            "page": document.metadata.get("page"),
        }
        for document in results
    ]

    return {
        "answer": answer,
        "sources": sources,
        "context_tokens": context_tokens,
    }