from app.loader import load_documents
from app.chunker import split_documents


def main():
    documents = load_documents()
    chunks = split_documents(documents)

    lengths = [len(chunk.page_content) for chunk in chunks]

    print(f"Documents loaded: {len(documents)}")
    print(f"Chunks created: {len(chunks)}")

    print("\n--- Chunk statistics ---")
    print(f"Shortest chunk: {min(lengths)} characters")
    print(f"Longest chunk: {max(lengths)} characters")
    print(f"Average chunk: {sum(lengths) / len(lengths):.2f} characters")

    print("\n--- First 10 chunks ---")

    for i, chunk in enumerate(chunks[:10]):
        print(f"\n===== CHUNK {i + 1} =====")
        print(f"Length: {len(chunk.page_content)}")
        print(f"Source: {chunk.metadata.get('source')}")
        print(f"Page: {chunk.metadata.get('page_label')}")
        print(f"Content:\n{chunk.page_content[:500]}")


if __name__ == "__main__":
    main()