"""
Stopword remover for Indonesian text processing.
"""

import re
from typing import List

from nahiarhdNLP.mydatasets.loaders import DatasetLoader


class StopwordRemover:
    """Remove stopwords from Indonesian text."""

    def __init__(self, language: str = "indonesian", **kwargs):
        """Initialize stopword remover.

        Args:
            language: Language code
            **kwargs: Additional arguments
        """
        self.language = language
        self.stopwords: List[str] = []
        self.custom_stopwords: List[str] = []

    def _load_data(self):
        """Load stopwords data from HuggingFace."""
        try:
            loader = DatasetLoader()
            dataset = loader.load_stopwords_dataset(language=self.language)

            self.stopwords = dataset

        except Exception as e:
            print(f"Warning: Could not load stopwords dataset: {e}")
            self._load_fallback_data()

    def _load_fallback_data(self):
        """Load fallback stopwords data."""
        # Basic Indonesian stopwords as fallback
        self.stopwords = [
            "yang",
            "dan",
            "di",
            "ke",
            "dari",
            "untuk",
            "dengan",
            "ini",
            "itu",
            "atau",
            "juga",
            "bisa",
            "akan",
            "sudah",
            "belum",
            "tidak",
            "bukan",
            "saya",
            "kamu",
            "dia",
            "mereka",
            "kami",
            "kita",
            "anda",
            "beliau",
            "mereka",
            "saya",
            "aku",
            "engkau",
            "kau",
            "kamu",
            "anda",
            "dia",
            "ia",
            "beliau",
            "mereka",
            "kami",
            "kita",
            "ini",
            "itu",
            "sini",
            "situ",
            "sana",
            "mana",
            "apa",
            "siapa",
            "kapan",
            "dimana",
            "kemana",
            "dari mana",
            "bagaimana",
            "mengapa",
            "kenapa",
            "berapa",
            "seberapa",
            "yang mana",
            "adalah",
            "ialah",
            "merupakan",
            "menjadi",
            "ada",
            "tidak ada",
            "bisa",
            "dapat",
            "mampu",
            "harus",
            "wajib",
            "perlu",
            "mesti",
            "sudah",
            "telah",
            "belum",
            "akan",
            "bakal",
            "mau",
            "ingin",
            "hendak",
            "akan",
            "sedang",
            "lagi",
            "masih",
            "sudah",
            "telah",
            "pernah",
            "belum pernah",
            "selalu",
            "sering",
            "kadang",
            "jarang",
            "tidak pernah",
            "sangat",
            "amat",
            "terlalu",
            "cukup",
            "agak",
            "sedikit",
            "banyak",
            "semua",
            "seluruh",
            "setiap",
            "masing-masing",
            "beberapa",
            "sebagian",
            "kebanyakan",
            "sebagian besar",
            "hampir",
            "hampir semua",
            "tidak ada",
            "tidak satupun",
            "sama sekali",
            "sama sekali tidak",
            "tidak sama sekali",
            "tidak pernah",
            "tidak akan",
            "tidak bisa",
            "tidak dapat",
            "tidak mampu",
            "tidak boleh",
            "tidak boleh",
            "tidak perlu",
            "tidak harus",
            "tidak wajib",
            "tidak mesti",
            "tidak mau",
            "tidak ingin",
            "tidak hendak",
            "tidak sedang",
            "tidak lagi",
            "tidak masih",
            "tidak sudah",
            "tidak telah",
            "tidak pernah",
            "tidak selalu",
            "tidak sering",
            "tidak kadang",
            "tidak jarang",
            "tidak sangat",
            "tidak amat",
            "tidak terlalu",
            "tidak cukup",
            "tidak agak",
            "tidak sedikit",
            "tidak banyak",
            "tidak semua",
            "tidak seluruh",
            "tidak setiap",
            "tidak masing-masing",
            "tidak beberapa",
            "tidak sebagian",
            "tidak kebanyakan",
            "tidak sebagian besar",
            "tidak hampir",
            "tidak hampir semua",
            "tidak ada",
            "tidak satupun",
            "sama sekali",
            "sama sekali tidak",
            "tidak sama sekali",
        ]

    def add_custom_stopwords(self, stopwords: List[str]):
        """Add custom stopwords to the list.

        Args:
            stopwords: List of custom stopwords to add
        """
        for stopword in stopwords:
            if stopword.lower() not in self.stopwords:
                self.custom_stopwords.append(stopword.lower())

    def remove_custom_stopwords(self, stopwords: List[str]):
        """Remove custom stopwords from the list.

        Args:
            stopwords: List of custom stopwords to remove
        """
        for stopword in stopwords:
            if stopword.lower() in self.custom_stopwords:
                self.custom_stopwords.remove(stopword.lower())

    def get_all_stopwords(self) -> List[str]:
        """Get all stopwords (default + custom).

        Returns:
            List of all stopwords
        """
        return self.stopwords + self.custom_stopwords

    def is_stopword(self, word: str) -> bool:
        """Check if a word is a stopword.

        Args:
            word: Word to check

        Returns:
            True if word is a stopword, False otherwise
        """
        return word.lower() in self.get_all_stopwords()

    def remove_stopwords(self, text: str) -> str:
        """Remove stopwords from text.

        Args:
            text: Input text

        Returns:
            Text with stopwords removed
        """
        if not text:
            return text

        # Split text into words
        words = text.split()

        # Filter out stopwords
        filtered_words = []
        for word in words:
            # Clean word (remove punctuation)
            clean_word = re.sub(r"[^\w\s]", "", word)
            if clean_word and not self.is_stopword(clean_word):
                filtered_words.append(word)
            elif not clean_word:  # Keep punctuation-only words
                filtered_words.append(word)

        return " ".join(filtered_words)

    def normalize(self, text: str) -> str:
        """Normalize text by removing stopwords.

        Args:
            text: Input text

        Returns:
            Text with stopwords removed
        """
        return self.remove_stopwords(text)

    def get_stopword_count(self) -> int:
        """Get number of stopwords.

        Returns:
            Number of stopwords
        """
        return len(self.get_all_stopwords())

    def get_custom_stopword_count(self) -> int:
        """Get number of custom stopwords.

        Returns:
            Number of custom stopwords
        """
        return len(self.custom_stopwords)

    def clear_custom_stopwords(self):
        """Clear all custom stopwords."""
        self.custom_stopwords.clear()

    def export_stopwords(self, filepath: str):
        """Export stopwords to file.

        Args:
            filepath: Path to export file
        """
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                for stopword in self.get_all_stopwords():
                    f.write(stopword + "\n")
            print(f"Stopwords exported to {filepath}")
        except Exception as e:
            print(f"Error exporting stopwords: {e}")

    def import_stopwords(self, filepath: str):
        """Import stopwords from file.

        Args:
            filepath: Path to import file
        """
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                stopwords = [line.strip() for line in f if line.strip()]
            self.add_custom_stopwords(stopwords)
            print(f"Imported {len(stopwords)} stopwords from {filepath}")
        except Exception as e:
            print(f"Error importing stopwords: {e}")
