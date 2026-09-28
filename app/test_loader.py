from app.loader import load_documents


def main():
    documents = load_documents()

    print(f"Number of documents/pages loaded: {len(documents)}")

    first_document = documents[0]

    print("\n--- Document type ---")
    print(type(first_document))

    print("\n--- Metadata ---")
    print(first_document.metadata)

    print("\n--- Content ---")
    print(first_document.page_content[:1000])


if __name__ == "__main__":
    main()