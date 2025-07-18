"""
Tokenizer for Indonesian text.
"""


class Tokenizer:
    """Memecah kalimat menjadi token (berdasarkan spasi)."""

    def tokenize(self, text: str) -> list:
        return text.split() if text else []
