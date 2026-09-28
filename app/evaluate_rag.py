from app.retriever import search_documents


EVALUATION_SET = [
    {
        "question": "What is LangChain?",
        "expected_pages": [3, 4],
    },
    {
        "question": "What is LangChain memory?",
        "expected_pages": [15],
    },
    {
        "question": "What are LangChain agents and tools?",
        "expected_pages": [23],
    },
    {
        "question": "How do I cook pasta?",
        "expected_pages": [],
    },
]


def evaluate_question(item):
    question = item["question"]
    expected_pages = set(item["expected_pages"])

    results = search_documents(question, k=3)

    retrieved_pages = {
        document.metadata.get("page")
        for document, _ in results
    }

    if not expected_pages:
        passed = len(results) == 0
    else:
        passed = bool(retrieved_pages.intersection(expected_pages))

    return {
        "question": question,
        "expected_pages": expected_pages,
        "retrieved_pages": retrieved_pages,
        "passed": passed,
    }


def main():
    passed_count = 0

    print("=" * 70)
    print("RAG RETRIEVAL EVALUATION")
    print("=" * 70)

    for item in EVALUATION_SET:
        result = evaluate_question(item)

        status = "PASS" if result["passed"] else "FAIL"

        print(f"\n[{status}] {result['question']}")
        print(f"Expected pages: {result['expected_pages']}")
        print(f"Retrieved pages: {result['retrieved_pages']}")

        if result["passed"]:
            passed_count += 1

    total = len(EVALUATION_SET)

    print("\n" + "=" * 70)
    print(f"RESULT: {passed_count}/{total} passed")
    print("=" * 70)


if __name__ == "__main__":
    main()