import re


INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"ignore\s+(all\s+)?prior\s+instructions",
    r"disregard\s+(all\s+)?previous\s+instructions",
    r"forget\s+(all\s+)?previous\s+instructions",
    r"reveal\s+(your\s+)?system\s+prompt",
    r"show\s+(me\s+)?your\s+system\s+prompt",
    r"print\s+(your\s+)?system\s+prompt",
    r"what\s+are\s+your\s+system\s+instructions",
    r"developer\s+message",
    r"override\s+(the\s+)?system",
    r"act\s+as\s+if\s+you\s+have\s+no\s+restrictions",
]


def detect_prompt_injection(text: str) -> bool:
    normalized_text = " ".join(text.lower().split())

    return any(
        re.search(pattern, normalized_text)
        for pattern in INJECTION_PATTERNS
    )


def validate_user_input(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("Question cannot be empty.")

    if detect_prompt_injection(text):
        raise ValueError(
            "The request was rejected by the security layer."
        )