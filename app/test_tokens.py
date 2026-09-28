from app.tokenizer import count_tokens


def main():
    texts = [
        "What is LangChain?",
        (
            "LangChain is an open-source framework designed to simplify "
            "the development of applications powered by large language models."
        ),
    ]

    for text in texts:
        print(f"\nText: {text}")
        print(f"Tokens: {count_tokens(text)}")


if __name__ == "__main__":
    main()