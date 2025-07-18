"""
nahiarhdNLP preprocessing module.
"""

from .cleaning.spell_corrector import SpellCorrector

# Import kelas-kelas untuk penggunaan advanced
from .cleaning.text_cleaner import TextCleaner
from .linguistic.stemmer import Stemmer
from .linguistic.stopwords import StopwordRemover
from .normalization.emoji import EmojiConverter
from .normalization.slang import SlangNormalizer
from .tokenization.tokenizer import Tokenizer

# Import semua fungsi utama dari utils
from .utils import (  # Fungsi dasar preprocessing; Fungsi-fungsi pembersihan individual; Fungsi pipeline dan preprocessing all-in-one
    clean_text,
    correct_spelling,
    emoji_to_words,
    pipeline,
    preprocess,
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
    replace_slang,
    replace_word_elongation,
    stem_text,
    to_lowercase,
    tokenize,
    words_to_emoji,
)

# Definisikan semua fungsi yang bisa diimport
__all__ = [
    # Fungsi dasar
    "remove_html",
    "remove_url",
    "remove_stopwords",
    "replace_slang",
    "replace_word_elongation",
    "emoji_to_words",
    "words_to_emoji",
    "correct_spelling",
    "stem_text",
    "tokenize",
    "clean_text",
    # Fungsi-fungsi pembersihan individual
    "remove_mentions",
    "remove_hashtags",
    "remove_numbers",
    "remove_punctuation",
    "remove_extra_spaces",
    "remove_special_chars",
    "remove_whitespace",
    "to_lowercase",
    # Fungsi pipeline
    "pipeline",
    "preprocess",
    # Kelas untuk advanced usage
    "TextCleaner",
    "SpellCorrector",
    "StopwordRemover",
    "Stemmer",
    "SlangNormalizer",
    "EmojiConverter",
    "Tokenizer",
]
