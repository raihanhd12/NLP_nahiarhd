"""
Slang normalizer for Indonesian and regional languages.
"""

import re
from typing import Dict, Optional

from nahiarhdNLP.datasets.loaders import DatasetLoader


class SlangNormalizer:
    """Normalizer for slang words."""

    def __init__(self, language: str = "indonesian", **kwargs):
        """Initialize slang normalizer.

        Args:
            language: Language code
            **kwargs: Additional arguments
        """
        self.language = language
        self.slang_dict: Dict[str, str] = {}

    def _load_data(self):
        """Load slang dictionary dari CSV."""
        try:
            loader = DatasetLoader()
            dataset = loader.load_slang_dataset(language=self.language)

            # Convert dataset to dictionary
            self.slang_dict = {}
            for item in dataset:
                slang_word = item.get("slang", "")
                formal_word = item.get("formal", "")
                if slang_word and formal_word:
                    self.slang_dict[slang_word.lower()] = formal_word.lower()
        except Exception as e:
            print(f"Warning: Could not load slang dataset for {self.language}: {e}")
            self.slang_dict = {}

    def normalize(self, text: str) -> str:
        """Normalize text by replacing slang words with formal words."""
        if not text:
            return text

        words = text.split()
        normalized_words = [self.slang_dict.get(word.lower(), word) for word in words]
        result = " ".join(normalized_words)
        # Bersihkan spasi ganda
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def add_slang_mapping(self, slang_word: str, formal_word: str):
        """Add custom slang mapping.

        Args:
            slang_word: Slang word
            formal_word: Formal word
        """
        self.slang_dict[slang_word.lower()] = formal_word.lower()

    def remove_slang_mapping(self, slang_word: str):
        """Remove slang mapping.

        Args:
            slang_word: Slang word to remove
        """
        if slang_word.lower() in self.slang_dict:
            del self.slang_dict[slang_word.lower()]

    def get_slang_count(self) -> int:
        """Get number of slang words in dictionary.

        Returns:
            Number of slang words
        """
        return len(self.slang_dict)

    def get_slang_mapping(self, slang_word: str) -> Optional[str]:
        """Get formal word for slang word.

        Args:
            slang_word: Slang word

        Returns:
            Formal word or None if not found
        """
        return self.slang_dict.get(slang_word.lower())


# Utilitas agar bisa diimport langsung
_slang_normalizer = SlangNormalizer()
_slang_normalizer._load_data()


def replace_slang(text: str) -> str:
    return _slang_normalizer.normalize(text)
