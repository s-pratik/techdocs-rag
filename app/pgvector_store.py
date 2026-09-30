from functools import lru_cache

from langchain_postgres import PGVector

from app.config import PGVECTOR_CONNECTION_STRING
from app.embeddings import get_embedding_model


COLLECTION_NAME = "techdocs"


@lru_cache(maxsize=1)
def get_pgvector_store():
    embeddings = get_embedding_model()

    vector_store = PGVector(
        embeddings=embeddings,
        collection_name=COLLECTION_NAME,
        connection=PGVECTOR_CONNECTION_STRING,
        embedding_length=1536,
        use_jsonb=True,
    )

    return vector_store