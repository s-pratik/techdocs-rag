from langchain_core.documents import Document

from app.context import build_context


def test_context_stays_within_budget():
    documents = [
        Document(
            page_content="This is a small test document.",
            metadata={
                "source": "test.pdf",
                "page": 1,
            },
        ),
        Document(
            page_content="This is another small test document.",
            metadata={
                "source": "test.pdf",
                "page": 2,
            },
        ),
    ]

    context, token_count = build_context(
        documents,
        max_tokens=100,
    )

    assert context
    assert token_count <= 100