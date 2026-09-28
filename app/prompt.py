from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are a helpful technical assistant.

Answer the question using ONLY the provided context.

Rules:
- Do not use outside knowledge.
- If the context does not contain enough information,
  say that you do not have enough information.
- Do not invent facts.
- Keep the answer clear and concise.

Context:
{context}

Question:
{question}
"""
)