from functools import lru_cache
from pathlib import Path

from langchain_chroma import Chroma

from app.embeddings import get_embedding_model


CHROMA_DIR = Path("chroma_db")
COLLECTION_NAME = "techdocs"


@lru_cache(maxsize=1)
def get_vector_store():
    embedding_model = get_embedding_model()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=str(CHROMA_DIR),
    )

    return vector_store