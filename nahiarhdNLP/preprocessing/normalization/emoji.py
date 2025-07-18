"""
Emoji normalizer for Indonesian text processing.
"""

import re
from typing import Dict, List, Optional

from nahiarhdNLP.mydatasets.loaders import DatasetLoader


class EmojiConverter:
    """Converter for emoji to Indonesian text and vice versa."""

    def __init__(self, language: str = "indonesian", **kwargs):
        """Initialize emoji converter.

        Args:
            language: Language code
            **kwargs: Additional arguments
        """
        self.language = language
        self.emoji_to_text: Dict[str, str] = {}
        self.text_to_emoji: Dict[str, str] = {}
        self.emoji_data: List[Dict] = []

    def _load_data(self):
        """Load emoji data from HuggingFace."""
        try:
            loader = DatasetLoader()
            dataset = loader.load_emoji_dataset(language=self.language)

            self.emoji_data = dataset

            # Build emoji to text mapping
            for item in dataset:
                emoji = item.get("emoji", "")
                name_id = item.get("name_id", "")
                alias = item.get("alias", "")

                if emoji and name_id:
                    self.emoji_to_text[emoji] = name_id

                # Also map alias to emoji for reverse conversion
                if emoji and alias:
                    self.text_to_emoji[alias.lower()] = emoji

                # Add name_id to reverse mapping
                if emoji and name_id:
                    self.text_to_emoji[name_id.lower()] = emoji

                # Add individual alias words
                aliases = item.get("aliases", [])
                if isinstance(aliases, list):
                    for alias_word in aliases:
                        if alias_word and emoji:
                            self.text_to_emoji[alias_word.lower()] = emoji

        except Exception as e:
            print(f"Warning: Could not load emoji dataset: {e}")
            self._load_fallback_data()

    def _load_fallback_data(self):
        """Load fallback emoji data."""
        # Basic fallback for common emojis
        self.emoji_to_text = {}

        # Build reverse mapping
        self.text_to_emoji = {v: k for k, v in self.emoji_to_text.items()}

    def emoji_to_text_convert(self, text: str) -> str:
        """Convert emoji to Indonesian text.

        Args:
            text: Text containing emojis

        Returns:
            Text with emojis converted to Indonesian words
        """
        if not text:
            return text

        result = text
        for emoji, indonesia_text in self.emoji_to_text.items():
            # Replace emoji with Indonesian text
            result = result.replace(emoji, f" {indonesia_text} ")

        # Clean up extra spaces
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def text_to_emoji_convert(self, text: str) -> str:
        """Convert Indonesian text to emoji.

        Args:
            text: Text containing Indonesian emoji descriptions

        Returns:
            Text with Indonesian emoji descriptions converted to emojis
        """
        if not text:
            return text

        result = text
        # Sort by length (longest first) to avoid partial matches
        sorted_texts = sorted(
            self.text_to_emoji.items(), key=lambda x: len(x[0]), reverse=True
        )

        for indonesia_text, emoji in sorted_texts:
            # Case insensitive replacement
            pattern = r"\b" + re.escape(indonesia_text) + r"\b"
            result = re.sub(pattern, emoji, result, flags=re.IGNORECASE)

        return result

    def normalize(self, text: str) -> str:
        """Normalize text by converting emoji to Indonesian text.

        Args:
            text: Input text

        Returns:
            Text with emojis converted to Indonesian words
        """
        return self.emoji_to_text_convert(text)

    def get_emoji_info(self, emoji: str) -> Optional[Dict]:
        """Get information about a specific emoji.

        Args:
            emoji: Emoji character

        Returns:
            Dictionary with emoji information or None if not found
        """
        for item in self.emoji_data:
            if item.get("emoji") == emoji:
                return item
        return None

    def search_emoji(self, query: str) -> List[Dict]:
        """Search for emojis by name or alias.

        Args:
            query: Search query

        Returns:
            List of matching emoji data
        """
        results = []
        query_lower = query.lower()

        for item in self.emoji_data:
            # Search in name_id
            if query_lower in item.get("name_id", "").lower():
                results.append(item)
                continue

            # Search in alias
            if query_lower in item.get("alias", "").lower():
                results.append(item)
                continue

            # Search in aliases list
            aliases = item.get("aliases", [])
            if isinstance(aliases, list):
                for alias in aliases:
                    if query_lower in alias.lower():
                        results.append(item)
                        break

        return results

    def get_emoji_count(self) -> int:
        """Get number of emojis in dataset.

        Returns:
            Number of emojis
        """
        return len(self.emoji_data)

    def get_categories(self) -> List[str]:
        """Get list of emoji categories.

        Returns:
            List of categories
        """
        categories = set()
        for item in self.emoji_data:
            category = item.get("category", "")
            if category:
                categories.add(category)
        return sorted(list(categories))

    def get_emojis_by_category(self, category: str) -> List[Dict]:
        """Get emojis by category.

        Args:
            category: Category name

        Returns:
            List of emoji data for the category
        """
        results = []
        for item in self.emoji_data:
            if item.get("category", "").lower() == category.lower():
                results.append(item)
        return results


# Utilitas agar bisa diimport langsung
_emoji_converter = EmojiConverter()
_emoji_converter._load_fallback_data()


def emoji_to_words(text: str) -> str:
    return _emoji_converter.emoji_to_text_convert(text)
