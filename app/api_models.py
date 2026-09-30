from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="Question to ask the RAG assistant",
    )


class Source(BaseModel):
    source: str
    page: int


class QueryResponse(BaseModel):
    answer: str
    sources: list[Source]
    context_tokens: int