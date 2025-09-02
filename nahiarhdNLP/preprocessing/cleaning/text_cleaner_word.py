"""
Text cleaner for Indonesian text processing.
"""

import re


class TextCleanerWord:
    """Clean and normalize Indonesian text."""

    def __init__(self, language: str = "indonesian", **kwargs):
        """Initialize text cleaner.

        Args:
            language: Language code
            **kwargs: Additional arguments
        """
        self.enable_html_cleaning = kwargs.get("enable_html_cleaning", True)
        self.enable_url_cleaning = kwargs.get("enable_url_cleaning", True)
        self.enable_mention_cleaning = kwargs.get("enable_mention_cleaning", True)
        self.enable_hashtag_cleaning = kwargs.get("enable_hashtag_cleaning", True)
        self.enable_email_cleaning = kwargs.get("enable_email_cleaning", False)
        self.enable_phone_cleaning = kwargs.get("enable_phone_cleaning", False)
        self.enable_currency_cleaning = kwargs.get("enable_currency_cleaning", False)

    def clean_urls(self, text: str, force: bool = False) -> str:
        """Remove URL protocols (http:// or https://) but keep the rest of the URL.

        Args:
            text: Input text
            force: Force remove protocols even if remove_urls flag is False

        Returns:
            Text with URL protocols removed
        """
        if not self.enable_url_cleaning and not force:
            return text

        # Pattern untuk URL protocols
        url_pattern = r"http[s]?://"
        result = re.sub(url_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_mentions(self, text: str, force: bool = False) -> str:
        """Remove @ from mentions but keep the username text.

        Args:
            text: Input text
            force: Force remove @ even if remove_mentions flag is False

        Returns:
            Text with @ removed from mentions
        """
        if not self.enable_mention_cleaning and not force:
            return text

        # Pattern untuk mentions, remove @ but keep the word
        mention_pattern = r"@(\w+)"
        result = re.sub(mention_pattern, r"\1", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_hashtags(self, text: str, force: bool = False) -> str:
        """Remove # from hashtags but keep the tag text.

        Args:
            text: Input text
            force: Force remove # even if remove_hashtags flag is False

        Returns:
            Text with # removed from hashtags
        """
        if not self.enable_hashtag_cleaning and not force:
            return text

        # Pattern untuk hashtags, remove # but keep the word
        hashtag_pattern = r"#(\w+)"
        result = re.sub(hashtag_pattern, r"\1", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_html(self, text: str, force: bool = False) -> str:
        """Remove HTML tags from text.

        Args:
            text: Input text with HTML tags
            force: Force remove HTML even if enable_html_cleaning flag is False

        Returns:
            Text with HTML tags removed
        """
        if not self.enable_html_cleaning and not force:
            return text

        # Pattern untuk HTML tags
        html_pattern = r"<[^>]+>"
        result = re.sub(html_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_emails(self, text: str, keep_text: bool = True) -> str:
        """Extract or remove email addresses from text.

        Args:
            text: Input text
            keep_text: If True, remove @ symbol from email but keep the text
                      If False, remove entire email

        Returns:
            Text with emails processed
        """
        if not self.enable_email_cleaning:
            return text

        if keep_text:
            # Remove @ and . from emails but keep the text parts
            # More comprehensive pattern to handle various email formats
            email_pattern = r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})"
            result = re.sub(email_pattern, r"\1 \2 \3", text)
        else:
            # Remove entire email
            email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            result = re.sub(email_pattern, "", text)

        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_phones(
        self, text: str, keep_numbers: bool = True, force: bool = False
    ) -> str:
        """Extract or remove phone numbers from text.

        Args:
            text: Input text
            keep_numbers: If True, remove formatting but keep numbers
                         If False, remove entire phone number
            force: Force cleaning even if enable_phone_cleaning is False

        Returns:
            Text with phone numbers processed
        """
        if not self.enable_phone_cleaning and not force:
            return text

        result = text
        if keep_numbers:
            # Remove phone formatting but keep numbers using regex substitution
            # Pattern to match phone numbers with formatting (more precise)
            phone_pattern = r"(\+62|62|0)([\d\-\(\)]{8,})(?=\s|$)|(\([\d]{3,4}\)\s?[\d\-\(\)]{6,})(?=\s|$)|([\+\d][\d\-\(\)]{8,})(?=\s|$)"

            def clean_phone_match(match):
                if match.group(1):  # Indonesian format (+62/62/0)
                    prefix = match.group(1)
                    numbers = re.sub(r"[\-\(\)\s]", "", match.group(2))
                    return prefix + numbers
                elif match.group(3):  # Parenthetical format like (021) 123-4567
                    numbers = re.sub(r"[\-\(\)\s]", "", match.group(3))
                    return numbers
                else:  # International format
                    numbers = re.sub(r"[\-\(\)\s]", "", match.group(4))
                    return numbers

            result = re.sub(phone_pattern, clean_phone_match, text)
        else:
            # Remove entire phone numbers
            phone_pattern = r"[\+]?[\d\-\(\)\s]{8,}\d"
            result = re.sub(phone_pattern, "", text)

        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_currency(self, text: str, keep_numbers: bool = True) -> str:
        """Clean currency symbols from text.

        Args:
            text: Input text
            keep_numbers: If True, remove currency symbols but keep numbers
                         If False, remove entire currency mentions

        Returns:
            Text with currency processed
        """
        if not self.enable_currency_cleaning:
            return text

        if keep_numbers:
            # Remove currency symbols but keep numbers
            currency_pattern = r"([$€£¥₹Rp\.,])(\d+(?:[\.,]\d+)*)"
            result = re.sub(currency_pattern, r"\2", text)
        else:
            # Remove entire currency mentions
            currency_pattern = r"[$€£¥₹Rp\.,]?\d+(?:[\.,]\d+)*[$€£¥₹Rp]?"
            result = re.sub(currency_pattern, "", text)

        result = re.sub(r"\s+", " ", result).strip()
        return result

    def get_options(self) -> dict:
        """Get current cleaning options.

        Returns:
            Dictionary of current options
        """
        return {
            "enable_html_cleaning": self.enable_html_cleaning,
            "enable_url_cleaning": self.enable_url_cleaning,
            "enable_mention_cleaning": self.enable_mention_cleaning,
            "enable_hashtag_cleaning": self.enable_hashtag_cleaning,
            "enable_email_cleaning": self.enable_email_cleaning,
            "enable_phone_cleaning": self.enable_phone_cleaning,
            "enable_currency_cleaning": self.enable_currency_cleaning,
        }
