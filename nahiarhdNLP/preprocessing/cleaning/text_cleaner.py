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
        self.remove_html = kwargs.get("remove_html", True)
        self.remove_urls = kwargs.get("remove_urls", True)
        self.remove_mentions = kwargs.get("remove_mentions", True)
        self.remove_hashtags = kwargs.get("remove_hashtags", True)
        self.remove_numbers = kwargs.get("remove_numbers", False)
        self.remove_punctuation = kwargs.get("remove_punctuation", False)
        self.remove_emoji = kwargs.get("remove_emoji", False)
        self.lowercase = kwargs.get("lowercase", True)
        self.remove_extra_spaces = kwargs.get("remove_extra_spaces", True)
        self.remove_repeated_chars = kwargs.get("remove_repeated_chars", True)
        self.remove_special_chars = kwargs.get("remove_special_chars", True)
        self.remove_whitespace = kwargs.get("remove_whitespace", True)

    def clean_urls(self, text: str, force: bool = False) -> str:
        """Remove URLs from text.

        Args:
            text: Input text
            force: Force remove URLs even if remove_urls flag is False

        Returns:
            Text with URLs removed
        """
        if not self.remove_urls and not force:
            return text

        # Pattern untuk URL
        url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        result = re.sub(url_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_mentions(self, text: str, force: bool = False) -> str:
        """Remove mentions (@username) from text.

        Args:
            text: Input text
            force: Force remove mentions even if remove_mentions flag is False

        Returns:
            Text with mentions removed
        """
        if not self.remove_mentions and not force:
            return text

        # Pattern untuk mentions
        mention_pattern = r"@\w+"
        result = re.sub(mention_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_hashtags(self, text: str, force: bool = False) -> str:
        """Remove hashtags (#tag) from text.

        Args:
            text: Input text
            force: Force remove hashtags even if remove_hashtags flag is False

        Returns:
            Text with hashtags removed
        """
        if not self.remove_hashtags and not force:
            return text

        # Pattern untuk hashtags
        hashtag_pattern = r"#\w+"
        result = re.sub(hashtag_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_numbers(self, text: str, force: bool = False) -> str:
        """Remove numbers from text.

        Args:
            text: Input text
            force: Force remove numbers even if remove_numbers flag is False

        Returns:
            Text with numbers removed
        """
        if not self.remove_numbers and not force:
            return text

        # Pattern untuk numbers
        number_pattern = r"\d+"
        result = re.sub(number_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_punctuation(self, text: str, force: bool = False) -> str:
        """Remove punctuation from text.

        Args:
            text: Input text
            force: Force remove punctuation even if remove_punctuation flag is False

        Returns:
            Text with punctuation removed
        """
        if not self.remove_punctuation and not force:
            return text

        # Pattern untuk punctuation
        punctuation_pattern = r"[^\w\s]"
        result = re.sub(punctuation_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

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
        result = re.sub(special_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_html(self, text: str, force: bool = False) -> str:
        """Remove HTML tags from text.

        Args:
            text: Input text with HTML tags
            force: Force remove HTML even if remove_html flag is False

        Returns:
            Text with HTML tags removed
        """
        if not self.remove_html and not force:
            return text

        # Pattern untuk HTML tags
        html_pattern = r"<[^>]+>"
        result = re.sub(html_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_emoji(self, text: str) -> str:
        """Remove emoji from text.

        Args:
            text: Input text with emoji

        Returns:
            Text with emoji removed
        """
        if not self.remove_emoji:
            return text

        # Pattern untuk emoji (Unicode ranges)
        # Menangkap semua karakter emoji berdasarkan Unicode blocks
        emoji_pattern = r"[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F700-\U0001F77F]|[\U0001F780-\U0001F7FF]|[\U0001F800-\U0001F8FF]|[\U0001F900-\U0001F9FF]|[\U0001FA00-\U0001FA6F]|[\U0001FA70-\U0001FAFF]|[\U00002600-\U000026FF]|[\U00002700-\U000027BF]"
        result = re.sub(emoji_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

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
        result = re.sub(r"\s+", " ", text).strip()
        return result

    def get_options(self) -> dict:
        """Get current cleaning options.

        Returns:
            Dictionary of current options
        """
        return {
            "remove_html": self.remove_html,
            "remove_urls": self.remove_urls,
            "remove_mentions": self.remove_mentions,
            "remove_hashtags": self.remove_hashtags,
            "remove_numbers": self.remove_numbers,
            "remove_punctuation": self.remove_punctuation,
            "remove_emoji": self.remove_emoji,
            "lowercase": self.lowercase,
            "remove_extra_spaces": self.remove_extra_spaces,
            "remove_repeated_chars": self.remove_repeated_chars,
            "remove_special_chars": self.remove_special_chars,
            "remove_whitespace": self.remove_whitespace,
        }
