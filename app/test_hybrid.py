from app.retriever import hybrid_search


def main():
    queries = [
        "What is LangChain memory?",
        "RunnableWithMessageHistory",
        "What are LangChain agents and tools?",
    ]

    for query in queries:
        print("\n" + "=" * 70)
        print(f"QUERY: {query}")
        print("=" * 70)

        results = hybrid_search(query, k=5)

        for i, document in enumerate(results, start=1):
            print(f"\n--- RESULT {i} ---")
            print(f"Source: {document.metadata.get('source')}")
            print(f"Page: {document.metadata.get('page')}")
            print(f"Content:\n{document.page_content[:400]}")


if __name__ == "__main__":
    main()