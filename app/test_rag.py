from app.rag import answer_question


def main():
    questions = [
        "What is LangChain?",
        "What is LangChain memory?",
        "How do I cook pasta?",
    ]

    for question in questions:
        print("\n" + "=" * 70)
        print(f"QUESTION: {question}")
        print("=" * 70)

        result = answer_question(question)

        print("\nANSWER:")
        print(result["answer"])

        print("\nCONTEXT TOKENS:")
        print(result["context_tokens"])

        print("\nSOURCES:")

        if not result["sources"]:
            print("No relevant sources found.")
            continue

        for source in result["sources"]:
            print(
                f"- {source['source']} | "
                f"Page {source['page']}"
            )


if __name__ == "__main__":
    main()