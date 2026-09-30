# TechDocs RAG Assistant

A production-oriented Retrieval-Augmented Generation (RAG) API built with
LangChain, Gemini embeddings, Supabase PGVector, BM25 hybrid retrieval,
Groq, FastAPI, and LangSmith.

## Architecture

PDF Documents
    ↓
Document Loader
    ↓
Text Chunking
    ↓
Gemini Embeddings
    ↓
Supabase PGVector
    ↓
Hybrid Retrieval
(Semantic + BM25)
    ↓
Token Budgeting
    ↓
Groq LLM
    ↓
Answer + Sources

LangSmith provides tracing and observability.

## Features

- PDF document ingestion
- Recursive text chunking
- Gemini embeddings
- Supabase PostgreSQL + pgvector
- Semantic similarity search
- BM25 keyword search
- Hybrid retrieval
- Token-aware context selection
- Source/page attribution
- Prompt-injection protection
- FastAPI REST API
- LangSmith tracing
- Automated tests with pytest

## Tech Stack

- Python
- LangChain
- Gemini Embeddings
- Groq
- ChromaDB (local development)
- Supabase / PostgreSQL / pgvector
- FastAPI
- BM25
- LangSmith
- pytest

## Project Structure

```text
app/
├── api_models.py
├── chunker.py
├── config.py
├── context.py
├── embeddings.py
├── loader.py
├── main.py
├── pgvector_store.py
├── prompt.py
├── rag.py
├── retriever.py
├── security.py
└── tokenizer.py

tests/
├── test_api.py
├── test_context.py
└── test_security.py

scripts/
└── index_pgvector.py