"""
Utility functions for preprocessing Indonesian text.
"""

from typing import List, Union

# Import kelas-kelas yang sudah ada
from .cleaning.text_cleaner import TextCleaner
from .cleaning.text_cleaner_word import TextCleaner as WordTextCleaner
from .linguistic.stemmer import Stemmer
from .linguistic.stopwords import StopwordRemover
from .normalization.emoji import EmojiConverter
from .normalization.spell_corrector import SpellCorrector
from .tokenization.tokenizer import Tokenizer

# Inisialisasi instance global untuk fungsi-fungsi utility (lazy loading)
_text_cleaner = None
_stopword_remover = None
_emoji_converter = None
_spell_corrector = None
_stemmer = None
_tokenizer = None


def _get_text_cleaner():
    global _text_cleaner
    if _text_cleaner is None:
        _text_cleaner = TextCleaner()
    return _text_cleaner


def _get_stopword_remover():
    global _stopword_remover
    if _stopword_remover is None:
        _stopword_remover = StopwordRemover()
        _stopword_remover._load_data()
    return _stopword_remover


def _get_emoji_converter():
    global _emoji_converter
    if _emoji_converter is None:
        _emoji_converter = EmojiConverter()
        _emoji_converter._load_data()
    return _emoji_converter


def _get_spell_corrector():
    global _spell_corrector
    if _spell_corrector is None:
        _spell_corrector = SpellCorrector()
    return _spell_corrector


def _get_stemmer():
    global _stemmer
    if _stemmer is None:
        _stemmer = Stemmer()
    return _stemmer


def _get_tokenizer():
    global _tokenizer
    if _tokenizer is None:
        _tokenizer = Tokenizer()
    return _tokenizer


def remove_html(text: str) -> str:
    """Menghapus HTML tags dari teks.

    Args:
        text: Teks yang mengandung HTML tags

    Returns:
        Teks tanpa HTML tags

    Example:
        >>> from src.preprocessing import remove_html
        >>> remove_html("website <a href='https://google.com'>google</a>")
        "website google"
    """
    if not text:
        return text

    return _get_text_cleaner().clean_html(text, force=True)


def remove_emoji(text: str) -> str:
    """Menghapus emoji dari teks.

    Args:
        text: Teks yang mengandung emoji

    Returns:
        Teks tanpa emoji

    Example:
        >>> from src.preprocessing import remove_emoji
        >>> remove_emoji("Halo dunia 😀😁 apa kabar? 🎉")
        "Halo dunia  apa kabar? "
    """
    if not text:
        return text

    # Buat TextCleaner dengan remove_emoji=True khusus untuk fungsi ini
    emoji_cleaner = TextCleaner(remove_emoji=True)
    return emoji_cleaner.clean_emoji(text)


def remove_url(text: str) -> str:
    """Menghapus URL dari teks.

    Args:
        text: Teks yang mengandung URL

    Returns:
        Teks tanpa URL

    Example:
        >>> from src.preprocessing import remove_url
        >>> remove_url("retrieved from https://gist.github.com/gruber/8891611")
        "retrieved from "
    """
    if not text:
        return text

    return _get_text_cleaner().clean_urls(text, force=True)


def remove_stopwords(text: str) -> str:
    """Menghapus stopwords dari teks.

    Args:
        text: Teks yang mengandung stopwords

    Returns:
        Teks tanpa stopwords

    Example:
        >>> from src.preprocessing import remove_stopwords
        >>> remove_stopwords("siapa yang suruh makan?!!")
        "  suruh makan?!!"
    """
    if not text:
        return text

    return _get_stopword_remover().remove_stopwords(text)


def replace_spell_corrector(text: str) -> str:
    """Mengganti kata gaul (slang) menjadi kata formal.

    Args:
        text: Teks yang mengandung kata slang

    Returns:
        Teks dengan kata formal

    Example:
        >>> from src.preprocessing import replace_spell_corrector
        >>> replace_spell_corrector("emg siapa yg nanya?")
        "memang siapa yang bertanya?"
    """
    if not text:
        return text

    # Menggunakan SpellCorrector yang sudah include slang normalization + spell correction
    return _get_spell_corrector().correct_sentence(text)


def replace_repeated_chars(text: str) -> str:
    """Mengatasi word elongation (karakter berulang).

    Args:
        text: Teks dengan karakter berulang

    Returns:
        Teks dengan karakter berulang dinormalisasi

    Example:
        >>> from src.preprocessing import replace_repeated_chars
        >>> replace_repeated_chars("kenapaaa?")
        "kenapa?"
    """
    if not text:
        return text

    return _get_text_cleaner().clean_repeated_chars(text)


def remove_mentions(text: str) -> str:
    """Menghapus mentions (@username) dari teks.

    Args:
        text: Teks yang mengandung mentions

    Returns:
        Teks tanpa mentions

    Example:
        >>> from src.preprocessing import remove_mentions
        >>> remove_mentions("Halo @user123 apa kabar?")
        "Halo  apa kabar?"
    """
    if not text:
        return text

    return _get_text_cleaner().clean_mentions(text, force=True)


def remove_hashtags(text: str) -> str:
    """Menghapus hashtags (#tag) dari teks.

    Args:
        text: Teks yang mengandung hashtags

    Returns:
        Teks tanpa hashtags

    Example:
        >>> from src.preprocessing import remove_hashtags
        >>> remove_hashtags("Hari ini #senin #libur")
        "Hari ini  "
    """
    if not text:
        return text

    return _get_text_cleaner().clean_hashtags(text, force=True)


def remove_numbers(text: str) -> str:
    """Menghapus angka dari teks.

    Args:
        text: Teks yang mengandung angka

    Returns:
        Teks tanpa angka

    Example:
        >>> from src.preprocessing import remove_numbers
        >>> remove_numbers("Saya berumur 25 tahun")
        "Saya berumur  tahun"
    """
    if not text:
        return text

    return _get_text_cleaner().clean_numbers(text, force=True)


def remove_punctuation(text: str) -> str:
    """Menghapus tanda baca dari teks.

    Args:
        text: Teks yang mengandung tanda baca

    Returns:
        Teks tanpa tanda baca

    Example:
        >>> from src.preprocessing import remove_punctuation
        >>> remove_punctuation("Halo, apa kabar?!")
        "Halo apa kabar"
    """
    if not text:
        return text

    return _get_text_cleaner().clean_punctuation(text, force=True)


def remove_extra_spaces(text: str) -> str:
    """Menghapus spasi berlebih dari teks.

    Args:
        text: Teks dengan spasi berlebih

    Returns:
        Teks dengan spasi normal

    Example:
        >>> from src.preprocessing import remove_extra_spaces
        >>> remove_extra_spaces("Halo    dunia   !")
        "Halo dunia !"
    """
    if not text:
        return text

    return _get_text_cleaner().clean_extra_spaces(text)


def remove_special_chars(text: str) -> str:
    """Menghapus karakter khusus yang bukan alfanumerik atau spasi.

    Args:
        text: Teks dengan karakter khusus

    Returns:
        Teks tanpa karakter khusus

    Example:
        >>> from src.preprocessing import remove_special_chars
        >>> remove_special_chars("Halo @#$%^&*() dunia!")
        "Halo  dunia!"
    """
    if not text:
        return text

    return _get_text_cleaner().clean_special_chars(text)


def remove_whitespace(text: str) -> str:
    """Membersihkan karakter whitespace (tab, newline, dll).

    Args:
        text: Teks dengan karakter whitespace

    Returns:
        Teks dengan whitespace dibersihkan

    Example:
        >>> from src.preprocessing import remove_whitespace
        >>> remove_whitespace("Halo\\n\\tdunia\\r")
        "Halo dunia"
    """
    if not text:
        return text

    return _get_text_cleaner().clean_whitespace(text)


def to_lowercase(text: str) -> str:
    """Mengubah teks menjadi huruf kecil.

    Args:
        text: Teks yang akan diubah

    Returns:
        Teks dalam huruf kecil

    Example:
        >>> from src.preprocessing import to_lowercase
        >>> to_lowercase("HALO Dunia")
        "halo dunia"
    """
    if not text:
        return text

    return _get_text_cleaner().to_lowercase(text)


def emoji_to_words(text: str) -> str:
    """Mengubah emoji menjadi kata-kata bahasa Indonesia.

    Args:
        text: Teks yang mengandung emoji

    Returns:
        Teks dengan emoji diubah menjadi kata

    Example:
        >>> from src.preprocessing import emoji_to_words
        >>> emoji_to_words("emoji 😀😁")
        "emoji wajah_gembira wajah_menyeringai"
    """
    if not text:
        return text

    return _get_emoji_converter().emoji_to_text_convert(text)


def words_to_emoji(text: str) -> str:
    """Mengubah kata-kata menjadi emoji.

    Args:
        text: Teks yang mengandung nama emoji dalam bahasa Indonesia

    Returns:
        Teks dengan kata diubah menjadi emoji

    Example:
        >>> from src.preprocessing import words_to_emoji
        >>> words_to_emoji("emoji wajah_gembira")
        "emoji 😀"
    """
    if not text:
        return text

    return _get_emoji_converter().text_to_emoji_convert(text)


def stem_text(text: str) -> str:
    """Melakukan stemming pada teks.

    Args:
        text: Teks yang akan di-stem

    Returns:
        Teks yang sudah di-stem

    Example:
        >>> from src.preprocessing import stem_text
        >>> stem_text("bermain-main dengan senang")
        "main main dengan senang"
    """
    if not text:
        return text

    return _get_stemmer().stem(text)


def tokenize(text: str) -> List[str]:
    """Memecah teks menjadi token.

    Args:
        text: Teks yang akan dipecah

    Returns:
        List token

    Example:
        >>> from src.preprocessing import tokenize
        >>> tokenize("Saya suka makan nasi")
        ["Saya", "suka", "makan", "nasi"]
    """
    if not text:
        return []

    return _get_tokenizer().tokenize(text)


class Pipeline:
    """
    Pipeline untuk menjalankan beberapa fungsi preprocessing secara berurutan.
    Bisa menerima functions langsung atau dictionary config.

    Example:
        >>> # Cara 1: Dengan functions
        >>> pipeline = Pipeline(remove_html, remove_url, remove_mentions)
        >>> result = pipeline.process("Hello <b>world</b> @user https://example.com")
        >>>
        >>> # Cara 2: Dengan config dictionary
        >>> config = {"remove_url": True, "remove_mentions": True, "to_lowercase": True}
        >>> pipeline = Pipeline(config)
        >>> result = pipeline.process("Hello @user https://example.com")
    """

    def __init__(self, *args):
        """
        Inisialisasi Pipeline dengan functions atau config dictionary.

        Args:
            *args: Functions yang akan dijalankan berurutan, atau config dictionary
        """
        if len(args) == 1 and isinstance(args[0], dict):
            # Mode config dictionary
            self.config = args[0]
            self.functions = None
            self._build_functions_from_config()
        else:
            # Mode functions
            self.functions = args
            self.config = None

    def _build_functions_from_config(self):
        """Build functions list dari config dictionary."""
        functions = []

        # Mapping config key ke function
        function_mapping = {
            "remove_html": globals().get("remove_html"),
            "remove_emoji": globals().get("remove_emoji"),
            "remove_url": globals().get("remove_url"),
            "remove_mentions": globals().get("remove_mentions"),
            "remove_hashtags": globals().get("remove_hashtags"),
            "remove_numbers": globals().get("remove_numbers"),
            "remove_special_chars": globals().get("remove_special_chars"),
            "remove_whitespace": globals().get("remove_whitespace"),
            "remove_extra_spaces": globals().get("remove_extra_spaces"),
            "replace_repeated_chars": globals().get("replace_repeated_chars"),
            "emoji_to_words": globals().get("emoji_to_words"),
            "words_to_emoji": globals().get("words_to_emoji"),
            "replace_spell_corrector": globals().get("replace_spell_corrector"),
            "remove_punctuation": globals().get("remove_punctuation"),
            "to_lowercase": globals().get("to_lowercase"),
            "remove_stopwords": globals().get("remove_stopwords"),
            "stem_text": globals().get("stem_text"),
            "tokenize": globals().get("tokenize"),
        }

        # Build functions berdasarkan config
        for key, enabled in self.config.items():
            if enabled and key in function_mapping and function_mapping[key]:
                functions.append(function_mapping[key])

        self.functions = tuple(functions)

    def process(self, text: str):
        """
        Memproses teks menggunakan semua functions yang sudah di-set.

        Args:
            text: Teks yang akan diproses

        Returns:
            Teks yang sudah diproses oleh semua functions
        """
        if not text:
            return text

        result = text
        for func in self.functions:
            result = func(result)
        return result

    def get_config(self) -> dict:
        """Get current configuration."""
        if self.config:
            return self.config.copy()
        else:
            # Generate config dari functions
            return {
                func.__name__: True
                for func in self.functions
                if hasattr(func, "__name__")
            }

    def get_enabled_steps(self) -> list:
        """Get list of enabled preprocessing steps."""
        if self.config:
            return [key for key, enabled in self.config.items() if enabled]
        else:
            return [
                func.__name__ for func in self.functions if hasattr(func, "__name__")
            ]

    def update_config(self, new_config: dict) -> None:
        """Update pipeline configuration."""
        if self.config:
            self.config.update(new_config)
            self._build_functions_from_config()
        else:
            # Convert dari function mode ke config mode
            current_config = self.get_config()
            current_config.update(new_config)
            self.config = current_config
            self._build_functions_from_config()

    def __call__(self, text: str):
        """Memungkinkan pipeline dipanggil langsung seperti function."""
        return self.process(text)

    def __repr__(self) -> str:
        """String representation."""
        if self.config:
            enabled = [k for k, v in self.config.items() if v]
            return f"Pipeline(config={enabled})"
        else:
            func_names = [
                func.__name__ for func in self.functions if hasattr(func, "__name__")
            ]
            return f"Pipeline({', '.join(func_names)})"


def pipeline(text: str, config: dict):
    """
    Fungsi helper untuk preprocessing dengan config dictionary.

    Args:
        text: Teks yang akan diproses
        config: Dictionary konfigurasi preprocessing

    Returns:
        Teks yang sudah diproses

    Example:
        >>> from nahiarhdNLP.preprocessing import pipeline
        >>>
        >>> # Preprocessing dengan config
        >>> config = {"remove_url": True, "to_lowercase": True}
        >>> result = pipeline("Hello https://example.com", config)
    """
    pipe = Pipeline(config)
    return pipe.process(text)


def preprocess(
    text: str,
    remove_html: bool = True,
    remove_emoji: bool = False,
    remove_url: bool = True,
    remove_mentions: bool = True,
    remove_hashtags: bool = True,
    remove_numbers: bool = False,
    remove_punctuation: bool = False,
    remove_special_chars: bool = True,
    remove_whitespace: bool = True,
    remove_extra_spaces: bool = True,
    to_lowercase: bool = True,
    replace_repeated_chars: bool = True,
    replace_spell_corrector: bool = True,
    emoji_to_words: bool = False,
    words_to_emoji: bool = False,
    remove_stopwords: bool = False,
    stem_text: bool = False,
    tokenize: bool = False,
) -> Union[str, List[str]]:
    """
    Fungsi preprocess dengan parameter eksplisit untuk setiap step.
    Untuk backward compatibility dan kontrol detail.

    Args:
        text: Teks yang akan diproses
        remove_html: Hapus HTML tags
        remove_emoji: Hapus emoji
        remove_url: Hapus URL
        remove_mentions: Hapus mentions (@user)
        remove_hashtags: Hapus hashtags (#tag)
        remove_numbers: Hapus angka
        remove_punctuation: Hapus tanda baca
        remove_special_chars: Hapus karakter khusus
        remove_whitespace: Hapus whitespace berlebih
        remove_extra_spaces: Hapus spasi berlebih
        to_lowercase: Ubah ke huruf kecil
        replace_repeated_chars: Normalisasi kata berulang
        replace_spell_corrector: Ganti kata slang dengan kata formal
        emoji_to_words: Ubah emoji ke kata
        words_to_emoji: Ubah kata ke emoji
        remove_stopwords: Hapus stopwords
        stem_text: Lakukan stemming
        tokenize: Tokenisasi (return list)

    Returns:
        Teks yang sudah diproses atau list token

    Example:
        >>> from nahiarhdNLP.preprocessing import preprocess
        >>>
        >>> # Preprocess basic
        >>> result = preprocess("Halooo @user!", replace_spell_corrector=True)
        >>>
        >>> # Preprocess dengan tokenisasi
        >>> tokens = preprocess("Saya suka makan", tokenize=True)
    """
    # Import fungsi-fungsi yang dibutuhkan di dalam scope ini untuk menghindari circular import

    # Build functions list berdasarkan parameter
    functions = []

    # Import fungsi di module level sudah ada, jadi bisa langsung pakai
    if remove_html:
        functions.append(globals()["remove_html"])
    if remove_emoji:
        functions.append(globals()["remove_emoji"])
    if remove_url:
        functions.append(globals()["remove_url"])
    if remove_mentions:
        functions.append(globals()["remove_mentions"])
    if remove_hashtags:
        functions.append(globals()["remove_hashtags"])
    if remove_numbers:
        functions.append(globals()["remove_numbers"])
    if remove_special_chars:
        functions.append(globals()["remove_special_chars"])
    if remove_whitespace:
        functions.append(globals()["remove_whitespace"])
    if remove_extra_spaces:
        functions.append(globals()["remove_extra_spaces"])
    if replace_repeated_chars:
        functions.append(globals()["replace_repeated_chars"])
    if emoji_to_words:
        functions.append(globals()["emoji_to_words"])
    if words_to_emoji:
        functions.append(globals()["words_to_emoji"])
    if replace_spell_corrector:
        functions.append(globals()["replace_spell_corrector"])
    if remove_punctuation:
        functions.append(globals()["remove_punctuation"])
    if to_lowercase:
        functions.append(globals()["to_lowercase"])
    if remove_stopwords:
        functions.append(globals()["remove_stopwords"])
    if stem_text:
        functions.append(globals()["stem_text"])
    if tokenize:
        functions.append(globals()["tokenize"])

    # Gunakan Pipeline baru untuk proses
    if functions:
        pipe = Pipeline(*functions)
        return pipe.process(text)
    else:
        return text


# Word-preserving text cleaning functions

_word_text_cleaner = None


def _get_word_text_cleaner():
    global _word_text_cleaner
    if _word_text_cleaner is None:
        _word_text_cleaner = WordTextCleaner()
    return _word_text_cleaner


def clean_urls_preserve_domain(text: str) -> str:
    """Remove URL protocols but keep domains.

    Args:
        text: Input text

    Returns:
        Text with URL protocols removed but domains preserved

    Example:
        >>> clean_urls_preserve_domain("Visit http://example.com")
        'Visit example.com'
    """
    cleaner = _get_word_text_cleaner()
    return cleaner.clean_urls(text, force=True)


def clean_mentions_preserve_username(text: str) -> str:
    """Remove @ symbols but keep usernames.

    Args:
        text: Input text

    Returns:
        Text with @ symbols removed but usernames preserved

    Example:
        >>> clean_mentions_preserve_username("Hello @user")
        'Hello user'
    """
    cleaner = _get_word_text_cleaner()
    return cleaner.clean_mentions(text, force=True)


def clean_hashtags_preserve_tags(text: str) -> str:
    """Remove # symbols but keep tag text.

    Args:
        text: Input text

    Returns:
        Text with # symbols removed but tag text preserved

    Example:
        >>> clean_hashtags_preserve_tags("I love #cars")
        'I love cars'
    """
    cleaner = _get_word_text_cleaner()
    return cleaner.clean_hashtags(text, force=True)


def clean_html_preserve_content(text: str) -> str:
    """Remove HTML tags but keep content.

    Args:
        text: Input text

    Returns:
        Text with HTML tags removed but content preserved

    Example:
        >>> clean_html_preserve_content("<p>Hello <b>world</b>!</p>")
        'Hello world!'
    """
    cleaner = _get_word_text_cleaner()
    return cleaner.clean_html(text, force=True)


def clean_all_preserve_words(
    text: str,
    clean_urls: bool = True,
    clean_mentions: bool = True,
    clean_hashtags: bool = True,
    clean_html: bool = True,
    clean_emails: bool = False,
    clean_phones: bool = False,
    clean_currency: bool = False,
) -> str:
    """Clean text while preserving meaningful words.

    Args:
        text: Input text
        clean_urls: Remove URL protocols but keep domains
        clean_mentions: Remove @ but keep usernames
        clean_hashtags: Remove # but keep tag text
        clean_html: Remove HTML tags but keep content
        clean_emails: Process email addresses
        clean_phones: Process phone numbers
        clean_currency: Process currency symbols

    Returns:
        Cleaned text with meaningful words preserved

    Example:
        >>> clean_all_preserve_words("Hello @user! Check #cars at http://example.com")
        'Hello user! Check cars at example.com'
    """
    cleaner = WordTextCleaner(
        remove_urls=clean_urls,
        remove_mentions=clean_mentions,
        remove_hashtags=clean_hashtags,
        remove_html=clean_html,
        clean_emails=clean_emails,
        clean_phones=clean_phones,
        clean_currency=clean_currency,
    )
    return cleaner.clean_all(text)


def clean_emails_preserve_text(text: str) -> str:
    """Clean email addresses while preserving the text content.

    Args:
        text: Input text containing emails

    Returns:
        Text with email addresses cleaned but text preserved

    Example:
        >>> clean_emails_preserve_text("Contact me at john.doe@gmail.com")
        'Contact me at john doe gmail com'
    """
    if not text:
        return text

    cleaner = WordTextCleaner(clean_emails=True)
    return cleaner.clean_emails(text)


def clean_phones_preserve_numbers(text: str) -> str:
    """Clean phone numbers while preserving the numbers.

    Args:
        text: Input text containing phone numbers

    Returns:
        Text with phone numbers cleaned but numbers preserved

    Example:
        >>> clean_phones_preserve_numbers("Call me at (555) 123-4567")
        'Call me at 5551234567'
    """
    if not text:
        return text

    cleaner = WordTextCleaner(clean_phones=True)
    return cleaner.clean_phones(text)


def clean_currency_preserve_numbers(text: str) -> str:
    """Clean currency symbols while preserving the numbers.

    Args:
        text: Input text containing currency

    Returns:
        Text with currency symbols removed but numbers preserved

    Example:
        >>> clean_currency_preserve_numbers("The price is $100.50")
        'The price is 100.50'
    """
    if not text:
        return text

    cleaner = WordTextCleaner(clean_currency=True)
    return cleaner.clean_currency(text)
