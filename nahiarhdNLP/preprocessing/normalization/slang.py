"""
Slang normalizer for Indonesian and regional languages.
"""

import re
from typing import Dict, Optional

from nahiarhdNLP.mydatasets.loaders import DatasetLoader


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
        """Load slang dictionary from HuggingFace."""
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
            self._load_fallback_data()

    def _load_fallback_data(self):
        """Load fallback slang data."""
        # Basic fallback for common Indonesian slang
        self.slang_dict = {
            "gw": "saya",
            "gue": "saya",
            "lo": "kamu",
            "lu": "kamu",
            "yg": "yang",
            "dgn": "dengan",
            "utk": "untuk",
            "dr": "dari",
            "sm": "sama",
            "tp": "tapi",
            "krn": "karena",
            "jd": "jadi",
            "sdh": "sudah",
            "udh": "sudah",
            "blm": "belum",
            "ga": "tidak",
            "gak": "tidak",
            "nggak": "tidak",
            "bgt": "banget",
            "bngt": "banget",
            "klo": "kalau",
            "kalo": "kalau",
            "gimana": "bagaimana",
            "gmn": "bagaimana",
            "kenapa": "mengapa",
            "knp": "mengapa",
            "makasih": "terima kasih",
            "mksh": "terima kasih",
            "org": "orang",
            "orng": "orang",
            "skrg": "sekarang",
            "skrng": "sekarang",
            "trs": "terus",
            "trus": "terus",
            "emg": "memang",
            "emang": "memang",
            "kyk": "seperti",
            "kyak": "seperti",
            "kayak": "seperti",
        }

    def normalize(self, text: str) -> str:
        """Normalize slang words in text.

        Args:
            text: Input text

        Returns:
            Text with normalized slang words
        """
        if not text:
            return text

        # Convert to lowercase for matching
        words = text.split()
        normalized_words = []

        for word in words:
            # Clean word for matching (remove punctuation)
            clean_word = re.sub(r"[^\w]", "", word.lower())

            # Check if word is in slang dictionary
            if clean_word in self.slang_dict:
                # Replace with formal word, preserving original case and punctuation
                formal_word = self.slang_dict[clean_word]

                # Preserve original punctuation
                if word.lower() != clean_word:
                    # Word has punctuation, preserve it
                    punctuation = re.sub(r"\w", "", word)
                    if word[0].isupper():
                        formal_word = formal_word.capitalize()
                    normalized_word = formal_word + punctuation
                else:
                    # No punctuation, just preserve case
                    if word[0].isupper():
                        formal_word = formal_word.capitalize()
                    normalized_word = formal_word

                normalized_words.append(normalized_word)
            else:
                normalized_words.append(word)

        return " ".join(normalized_words)

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
_slang_normalizer._load_fallback_data()


def replace_slang(text: str) -> str:
    return _slang_normalizer.normalize(text)
