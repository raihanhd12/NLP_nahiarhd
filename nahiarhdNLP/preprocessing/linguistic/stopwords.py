"""
Stopword remover for Indonesian text processing.
"""

import re
from typing import List

from nahiarhdNLP.datasets.loaders import DatasetLoader


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
        """Load stopwords data dari CSV."""
        try:
            loader = DatasetLoader()
            dataset = loader.load_stopwords_dataset(language=self.language)
            self.stopwords = dataset
        except Exception as e:
            print(f"Warning: Could not load stopwords dataset: {e}")
            self.stopwords = []

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
        """Remove stopwords from text."""
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

        result = " ".join(filtered_words)
        # Bersihkan spasi ganda
        result = re.sub(r"\s+", " ", result).strip()
        return result

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
