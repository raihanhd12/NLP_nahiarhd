"""
nahiarhdNLP.preprocessing - Indonesian text preprocessing utilities

This module provides comprehensive text preprocessing functionality for Indonesian language,
including cleaning, normalization, tokenization, and linguistic processing.
"""

# Import all classes for advanced usage
from .cleaning.text_cleaner import TextCleaner
from .linguistic.stemmer import Stemmer
from .linguistic.stopwords import StopwordRemover
from .normalization.emoji import EmojiConverter
from .normalization.spell_corrector import SpellCorrector
from .tokenization.tokenizer import Tokenizer

# Import all individual utility functions
from .utils import (  # Basic cleaning functions; Normalization and correction functions; Emoji functions; Linguistic functions; Pipeline functions; Word-preserving cleaning functions
    Pipeline,
    clean_all_preserve_words,
    clean_currency_preserve_numbers,
    clean_emails_preserve_text,
    clean_hashtags_preserve_tags,
    clean_html_preserve_content,
    clean_mentions_preserve_username,
    clean_phones_preserve_numbers,
    clean_urls_preserve_domain,
    emoji_to_words,
    pipeline,
    preprocess,
    remove_emoji,
    remove_extra_spaces,
    remove_hashtags,
    remove_html,
    remove_mentions,
    remove_numbers,
    remove_punctuation,
    remove_special_chars,
    remove_stopwords,
    remove_url,
    remove_whitespace,
    replace_repeated_chars,
    replace_spell_corrector,
    stem_text,
    to_lowercase,
    tokenize,
    words_to_emoji,
)

# Define what gets imported with "from nahiarhdNLP.preprocessing import *"
__all__ = [
    # Individual functions
    "remove_html",
    "remove_emoji",
    "remove_url",
    "remove_mentions",
    "remove_hashtags",
    "remove_numbers",
    "remove_punctuation",
    "remove_extra_spaces",
    "remove_special_chars",
    "remove_whitespace",
    "to_lowercase",
    "replace_spell_corrector",
    "replace_repeated_chars",
    "emoji_to_words",
    "words_to_emoji",
    "remove_stopwords",
    "stem_text",
    "tokenize",
    # Pipeline functions
    "Pipeline",
    "pipeline",
    "preprocess",
    # Classes
    "TextCleaner",
    "Stemmer",
    "StopwordRemover",
    "EmojiConverter",
    "SpellCorrector",
    "Tokenizer",
    # Word-preserving cleaning functions
    "clean_urls_preserve_domain",
    "clean_mentions_preserve_username",
    "clean_hashtags_preserve_tags",
    "clean_html_preserve_content",
    "clean_emails_preserve_text",
    "clean_phones_preserve_numbers",
    "clean_currency_preserve_numbers",
    "clean_all_preserve_words",
]
