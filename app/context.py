from app.tokenizer import count_tokens


MAX_CONTEXT_TOKENS = 2000


def build_context(results, max_tokens=MAX_CONTEXT_TOKENS):
    selected_chunks = []
    total_tokens = 0

    for document in results:
        source = document.metadata.get("source")
        page = document.metadata.get("page")

        chunk_text = (
            f"[Source: {source}, Page: {page}]\n"
            f"{document.page_content}"
        )

        chunk_tokens = count_tokens(chunk_text)

        if total_tokens + chunk_tokens > max_tokens:
            continue

        selected_chunks.append(chunk_text)
        total_tokens += chunk_tokens

    context = "\n\n".join(selected_chunks)

    return context, total_tokens