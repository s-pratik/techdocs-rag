from pathlib import Path

from langchain_community.document_loaders import PyPDFDirectoryLoader


DOCUMENTS_DIR = Path("data/documents")


def load_documents():
    loader = PyPDFDirectoryLoader(str(DOCUMENTS_DIR))

    documents = loader.load()

    for document in documents:
        source = Path(document.metadata["source"]).name

        document.metadata = {
            "source": source,
            "page": document.metadata["page"] + 1,
            "total_pages": document.metadata.get("total_pages"),
        }

    return documents