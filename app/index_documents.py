import hashlib
import time

from app.chunker import split_documents
from app.loader import load_documents
from app.vectorstore import get_vector_store


BATCH_SIZE = 80
WAIT_SECONDS = 60


def create_chunk_id(chunk):
    content = (
        f"{chunk.metadata['source']}"
        f"|{chunk.metadata['page']}"
        f"|{chunk.page_content}"
    )

    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def main():
    print("Loading documents...")
    documents = load_documents()

    print(f"Loaded {len(documents)} documents/pages.")

    print("Splitting documents...")
    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating/opening Chroma vector store...")
    vector_store = get_vector_store()

    ids = [create_chunk_id(chunk) for chunk in chunks]

    total_batches = (len(chunks) + BATCH_SIZE - 1) // BATCH_SIZE

    for batch_number, start in enumerate(
        range(0, len(chunks), BATCH_SIZE),
        start=1,
    ):
        end = min(start + BATCH_SIZE, len(chunks))

        batch_chunks = chunks[start:end]
        batch_ids = ids[start:end]

        print(
            f"\nProcessing batch {batch_number}/{total_batches} "
            f"({len(batch_chunks)} chunks)..."
        )

        vector_store.add_documents(
            documents=batch_chunks,
            ids=batch_ids,
        )

        print(f"Batch {batch_number} completed.")

        if batch_number < total_batches:
            print(f"Waiting {WAIT_SECONDS} seconds for rate limit...")
            time.sleep(WAIT_SECONDS)

    print("\nIndexing complete.")


if __name__ == "__main__":
    main()