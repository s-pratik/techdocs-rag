import tiktoken


MODEL_NAME = "gpt-oss-20b"


def get_tokenizer():
    return tiktoken.encoding_for_model(MODEL_NAME)


def count_tokens(text: str) -> int:
    tokenizer = get_tokenizer()

    return len(tokenizer.encode(text))