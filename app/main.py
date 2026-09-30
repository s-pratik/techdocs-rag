from fastapi import FastAPI, HTTPException

from app.api_models import QueryRequest, QueryResponse
from app.rag import answer_question
from app.security import detect_prompt_injection


app = FastAPI(
    title="TechDocs RAG API",
    description="Production-oriented RAG API using LangChain.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "TechDocs RAG API is running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    if detect_prompt_injection(request.question):
        raise HTTPException(
            status_code=400,
            detail="The request was rejected by the security layer.",
        )

    try:
        return answer_question(request.question)

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing the question.",
        ) from exc