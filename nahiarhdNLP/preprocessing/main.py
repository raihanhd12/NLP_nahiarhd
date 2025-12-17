"""
Main functions for preprocessing Indonesian text.
"""

# Import kelas-kelas yang sudah ada
from .cleaning.text_cleaner import TextCleaner
from .cleaning.text_cleaner_word import TextCleanerWord as WordTextCleaner
from .cleaning.text_replace import TextReplace
from .linguistic.stemmer import Stemmer
from .linguistic.stopword import StopwordRemover
from .normalization.emoji import EmojiConverter
from .normalization.spell_corrector import SpellCorrector
from .tokenization.tokenizer import Tokenizer

# Inisialisasi instance global untuk fungsi-fungsi utility (lazy loading)
_text_cleaner = None
_text_cleaner_word = None
_text_replace = None
_stemmer = None
_stopword = None
_emoji = None
_spell_corrector = None
_tokenizer = None


def _get_text_cleaner():
    global _text_cleaner
    if _text_cleaner is None:
        _text_cleaner = TextCleaner()
    return _text_cleaner


def _get_text_cleaner_word():
    global _text_cleaner_word
    if _text_cleaner_word is None:
        _text_cleaner_word = WordTextCleaner()
    return _text_cleaner_word


def _get_text_replace():
    global _text_replace
    if _text_replace is None:
        _text_replace = TextReplace()
    return _text_replace


def _get_stemmer():
    global _stemmer
    if _stemmer is None:
        _stemmer = Stemmer()
    return _stemmer


def _get_stopword():
    global _stopword
    if _stopword is None:
        _stopword = StopwordRemover()
        _stopword._load_data()
    return _stopword


def _get_emoji():
    global _emoji
    if _emoji is None:
        _emoji = EmojiConverter()
        _emoji._load_data()
    return _emoji


def _get_spell_corrector():
    global _spell_corrector
    if _spell_corrector is None:
        _spell_corrector = SpellCorrector()
    return _spell_corrector


def _get_tokenizer():
    global _tokenizer
    if _tokenizer is None:
        _tokenizer = Tokenizer()
    return _tokenizer


class Pipeline:
    """
    Pipeline config-only: hanya menerima dict config {step_name: True/False}.
    """

    def __init__(self, config: dict):
        if not isinstance(config, dict):
            raise TypeError("config must be a dict of {step_name: True/False}")
        self.config = config
        self.functions = tuple()
        self._build_functions_from_config()

    def _build_functions_from_config(self):

        # mapping step -> callable (internal only)
        # Use class methods bound at call-time to avoid instance attributes shadowing methods
        function_mapping = {
            "remove_html": lambda t, _m=TextCleaner.remove_html: _m(_get_text_cleaner(), t),
            "remove_urls": lambda t, _m=TextCleaner.remove_urls: _m(_get_text_cleaner(), t),
            "remove_mentions": lambda t, _m=TextCleaner.remove_mentions: _m(_get_text_cleaner(), t),
            "remove_hashtags": lambda t, _m=TextCleaner.remove_hashtags: _m(_get_text_cleaner(), t),
            "remove_punctuation": lambda t, _m=TextCleaner.remove_punctuation: _m(_get_text_cleaner(), t),
            "remove_emoji": lambda t, _m=TextCleaner.remove_emoji: _m(_get_text_cleaner(), t),
            "remove_lowercase": lambda t, _m=TextCleaner.remove_lowercase: _m(_get_text_cleaner(), t),
            "remove_extra_spaces": lambda t, _m=TextCleaner.remove_extra_spaces: _m(_get_text_cleaner(), t),
            "remove_repeated_chars": lambda t, _m=TextCleaner.remove_repeated_chars: _m(_get_text_cleaner(), t),
            "remove_special_chars": lambda t, _m=TextCleaner.remove_special_chars: _m(_get_text_cleaner(), t),
            "remove_whitespace": lambda t, _m=TextCleaner.remove_whitespace: _m(_get_text_cleaner(), t),
            "remove_emails": lambda t, _m=TextCleaner.remove_emails: _m(_get_text_cleaner(), t),
            "remove_phones": lambda t, _m=TextCleaner.remove_phones: _m(_get_text_cleaner(), t),
            "remove_currency": lambda t, _m=TextCleaner.remove_currency: _m(_get_text_cleaner(), t),
            "remove_numbers": lambda t, _m=TextCleaner.remove_numbers: _m(_get_text_cleaner(), t),
            "clean_urls": lambda t, _m=WordTextCleaner.clean_urls: _m(_get_text_cleaner_word(), t),
            "clean_mentions": lambda t, _m=WordTextCleaner.clean_mentions: _m(_get_text_cleaner_word(), t),
            "clean_hashtags": lambda t, _m=WordTextCleaner.clean_hashtags: _m(_get_text_cleaner_word(), t),
            "clean_html": lambda t, _m=WordTextCleaner.clean_html: _m(_get_text_cleaner_word(), t),
            "replace_email": lambda t, _m=TextReplace.replace_email: _m(_get_text_replace(), t),
            "replace_link": lambda t, _m=TextReplace.replace_link: _m(_get_text_replace(), t),
            "replace_user": lambda t, _m=TextReplace.replace_user: _m(_get_text_replace(), t),
            "stem": lambda t, _m=Stemmer.stem: _m(_get_stemmer(), t),
            "stopword": lambda t, _m=StopwordRemover.remove_stopwords: _m(_get_stopword(), t),
            "emoji_to_text": lambda t, _m=EmojiConverter.emoji_to_text_convert: _m(_get_emoji(), t),
            "text_to_emoji": lambda t, _m=EmojiConverter.text_to_emoji_convert: _m(_get_emoji(), t),
            "spell_corrector_word": lambda t, _m=SpellCorrector.correct_word: _m(_get_spell_corrector(), t),
            "spell_corrector_sentence": lambda t, _m=SpellCorrector.correct_sentence: _m(_get_spell_corrector(), t),
            "tokenizer": lambda t, _m=Tokenizer.tokenize: _m(_get_tokenizer(), t),
        }

        functions = []
        unknown_steps = []

        for key, enabled in self.config.items():
            if not enabled:
                continue

            func = function_mapping.get(key)

            if func is None:
                unknown_steps.append(key)
                continue

            functions.append(func)

        if unknown_steps:
            raise ValueError(
                f"Unknown preprocessing steps: {unknown_steps}. "
                f"Available: {sorted(function_mapping.keys())}"
            )

        self.functions = tuple(functions)

    def process(self, text: str):
        if not text:
            return text
        result = text
        for func in self.functions:
            result = func(result)
        return result

    def update_config(self, new_config: dict) -> None:
        if not isinstance(new_config, dict):
            raise TypeError("new_config must be dict {step_name: True/False}")
        self.config.update(new_config)
        self._build_functions_from_config()

    def get_enabled_steps(self) -> list:
        return [k for k, v in self.config.items() if v]

    def __call__(self, text: str):
        return self.process(text)

    def __repr__(self) -> str:
        return f"Pipeline(config={self.get_enabled_steps()})"
