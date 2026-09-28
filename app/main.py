from fastapi import FastAPI


app = FastAPI(
    title="TechDocs RAG API",
    description="A production-oriented RAG API built with LangChain.",
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