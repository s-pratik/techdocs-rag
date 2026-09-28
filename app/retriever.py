from langchain_community.retrievers import BM25Retriever

from app.chunker import split_documents
from app.loader import load_documents
from app.vectorstore import get_vector_store


DEFAULT_K = 3
DEFAULT_MAX_DISTANCE = 0.70


def search_documents(
    query: str,
    k: int = DEFAULT_K,
    max_distance: float = DEFAULT_MAX_DISTANCE,
):
    vector_store = get_vector_store()

    results = vector_store.similarity_search_with_score(
        query,
        k=k,
    )

    return [
        (document, score)
        for document, score in results
        if score <= max_distance
    ]


_bm25_retriever = None


def get_bm25_retriever(k: int = 5):
    global _bm25_retriever

    if _bm25_retriever is None:
        documents = load_documents()
        chunks = split_documents(documents)

        _bm25_retriever = BM25Retriever.from_documents(
            chunks,
            k=k,
        )

    _bm25_retriever.k = k

    return _bm25_retriever


def hybrid_search(
    query: str,
    k: int = 5,
):
    # Semantic search
    vector_results = search_documents(
        query,
        k=k,
    )

    if not vector_results:
        return []

    
    # Keyword search
    bm25_retriever = get_bm25_retriever(k=k)
    bm25_results = bm25_retriever.invoke(query)

    # Combine the two result lists using rank.
    ranked_documents = {}

    for rank, (document, _) in enumerate(vector_results, start=1):
        key = document.page_content

        ranked_documents.setdefault(
            key,
            {
                "document": document,
                "score": 0,
            },
        )

        ranked_documents[key]["score"] += 1 / rank

    for rank, document in enumerate(bm25_results, start=1):
        key = document.page_content

        ranked_documents.setdefault(
            key,
            {
                "document": document,
                "score": 0,
            },
        )

        ranked_documents[key]["score"] += 1 / rank

    ranked_results = sorted(
        ranked_documents.values(),
        key=lambda item: item["score"],
        reverse=True,
    )

    return [
        item["document"]
        for item in ranked_results[:k]
    ]