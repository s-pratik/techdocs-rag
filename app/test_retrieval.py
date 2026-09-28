from app.retriever import search_documents, print_search_results


def main():
    queries = [
        "What is LangChain?",
        "What is LangChain memory?",
        "How do I cook pasta?",
    ]

    for query in queries:
        results = search_documents(query, k=5)
        print_search_results(query, results)


if __name__ == "__main__":
    main()