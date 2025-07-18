"""
Text cleaner for Indonesian text processing.
"""

import re


class TextCleaner:
    """Clean and normalize Indonesian text."""

    def __init__(self, language: str = "indonesian", **kwargs):
        """Initialize text cleaner.

        Args:
            language: Language code
            **kwargs: Additional arguments
        """
        self.remove_urls = kwargs.get("remove_urls", True)
        self.remove_mentions = kwargs.get("remove_mentions", True)
        self.remove_hashtags = kwargs.get("remove_hashtags", True)
        self.remove_numbers = kwargs.get("remove_numbers", False)
        self.remove_punctuation = kwargs.get("remove_punctuation", False)
        self.lowercase = kwargs.get("lowercase", True)
        self.remove_extra_spaces = kwargs.get("remove_extra_spaces", True)
        self.remove_repeated_chars = kwargs.get("remove_repeated_chars", True)

    def clean_urls(self, text: str) -> str:
        """Remove URLs from text.

        Args:
            text: Input text

        Returns:
            Text with URLs removed
        """
        if not self.remove_urls:
            return text

        # Pattern untuk URL
        url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        return re.sub(url_pattern, "", text)

    def clean_mentions(self, text: str) -> str:
        """Remove mentions (@username) from text.

        Args:
            text: Input text

        Returns:
            Text with mentions removed
        """
        if not self.remove_mentions:
            return text

        # Pattern untuk mentions
        mention_pattern = r"@\w+"
        return re.sub(mention_pattern, "", text)

    def clean_hashtags(self, text: str) -> str:
        """Remove hashtags (#tag) from text.

        Args:
            text: Input text

        Returns:
            Text with hashtags removed
        """
        if not self.remove_hashtags:
            return text

        # Pattern untuk hashtags
        hashtag_pattern = r"#\w+"
        return re.sub(hashtag_pattern, "", text)

    def clean_numbers(self, text: str) -> str:
        """Remove numbers from text.

        Args:
            text: Input text

        Returns:
            Text with numbers removed
        """
        if not self.remove_numbers:
            return text

        # Pattern untuk numbers
        number_pattern = r"\d+"
        return re.sub(number_pattern, "", text)

    def clean_punctuation(self, text: str) -> str:
        """Remove punctuation from text.

        Args:
            text: Input text

        Returns:
            Text with punctuation removed
        """
        if not self.remove_punctuation:
            return text

        # Pattern untuk punctuation
        punctuation_pattern = r"[^\w\s]"
        return re.sub(punctuation_pattern, "", text)

    def to_lowercase(self, text: str) -> str:
        """Convert text to lowercase.

        Args:
            text: Input text

        Returns:
            Lowercase text
        """
        if not self.lowercase:
            return text

        return text.lower()

    def clean_extra_spaces(self, text: str) -> str:
        """Remove extra whitespace from text.

        Args:
            text: Input text

        Returns:
            Text with extra spaces removed
        """
        if not self.remove_extra_spaces:
            return text

        # Replace multiple spaces with single space
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def clean_repeated_chars(self, text: str) -> str:
        """Remove repeated characters (e.g., 'bangetttt' -> 'banget').

        Args:
            text: Input text

        Returns:
            Text with repeated characters normalized
        """
        if not self.remove_repeated_chars:
            return text

        # Pattern untuk repeated characters (3+ times)
        repeated_pattern = r"(.)\1{2,}"
        return re.sub(repeated_pattern, r"\1\1", text)

    def clean_special_chars(self, text: str) -> str:
        """Remove special characters that are not alphanumeric or spaces.

        Args:
            text: Input text

        Returns:
            Text with special characters removed
        """
        # Keep alphanumeric, spaces, and common punctuation
        special_pattern = r'[^\w\s.,!?;:()"\'-]'
        return re.sub(special_pattern, "", text)

    def clean_whitespace(self, text: str) -> str:
        """Clean whitespace characters.

        Args:
            text: Input text

        Returns:
            Text with cleaned whitespace
        """
        # Replace tabs, newlines, etc. with spaces
        text = re.sub(r"\t", " ", text)
        text = re.sub(r"\n", " ", text)
        text = re.sub(r"\r", " ", text)
        return text

    def clean(self, text: str) -> str:
        """Clean text using all cleaning methods.

        Args:
            text: Input text

        Returns:
            Cleaned text
        """
        if not text:
            return text

        # Apply cleaning steps in order
        text = self.clean_whitespace(text)
        text = self.clean_urls(text)
        text = self.clean_mentions(text)
        text = self.clean_hashtags(text)
        text = self.clean_special_chars(text)
        text = self.clean_numbers(text)
        text = self.clean_punctuation(text)
        text = self.clean_repeated_chars(text)
        text = self.to_lowercase(text)
        text = self.clean_extra_spaces(text)

        return text

    def normalize(self, text: str) -> str:
        """Normalize text by cleaning it.

        Args:
            text: Input text

        Returns:
            Cleaned and normalized text
        """
        return self.clean(text)

    def set_options(self, **kwargs):
        """Set cleaning options.

        Args:
            **kwargs: Cleaning options to set
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_options(self) -> dict:
        """Get current cleaning options.

        Returns:
            Dictionary of current options
        """
        return {
            "remove_urls": self.remove_urls,
            "remove_mentions": self.remove_mentions,
            "remove_hashtags": self.remove_hashtags,
            "remove_numbers": self.remove_numbers,
            "remove_punctuation": self.remove_punctuation,
            "lowercase": self.lowercase,
            "remove_extra_spaces": self.remove_extra_spaces,
            "remove_repeated_chars": self.remove_repeated_chars,
        }
