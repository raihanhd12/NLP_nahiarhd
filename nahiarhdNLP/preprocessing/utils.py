"""
Utility functions for preprocessing Indonesian text.
"""

from typing import List, Union

# Import kelas-kelas yang sudah ada
from .cleaning.text_cleaner import TextCleaner
from .cleaning.text_cleaner_word import TextCleanerWord as WordTextCleaner
from .linguistic.stemmer import Stemmer
from .linguistic.stopwords import StopwordRemover
from .normalization.emoji import EmojiConverter
from .normalization.spell_corrector import SpellCorrector
from .tokenization.tokenizer import Tokenizer

# Inisialisasi instance global untuk fungsi-fungsi utility (lazy loading)
_text_cleaner = None
_text_cleaner_word = None
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


def _get_text_cleaner_word():
    global _text_cleaner_word
    if _text_cleaner_word is None:
        _text_cleaner_word = WordTextCleaner()
    return _text_cleaner_word


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


def enable_html_cleaning(text: str) -> str:
    """Mengaktifkan pembersihan HTML pada teks.

    Args:
        text: Teks yang akan dibersihkan

    Returns:
        Teks tanpa tag HTML

    Example:
        >>> from src.preprocessing import enable_html_cleaning
        >>> enable_html_cleaning("Hello <b>world</b>")
        "Hello world"
    """
    if not text:
        return text

    return _get_text_cleaner_word().enable_html_cleaning(text)


def enable_url_cleaning(text: str) -> str:
    """Mengaktifkan pembersihan URL pada teks.

    Args:
        text: Teks yang akan dibersihkan

    Returns:
        Teks tanpa URL

    Example:
        >>> from src.preprocessing import enable_url_cleaning
        >>> enable_url_cleaning("Kunjungi https://example.com")
        "Kunjungi "
    """
    if not text:
        return text

    return _get_text_cleaner_word().enable_url_cleaning(text)


def enable_mention_cleaning(text: str) -> str:
    """Mengaktifkan pembersihan mention pada teks.

    Args:
        text: Teks yang akan dibersihkan

    Returns:
        Teks tanpa mention

    Example:
        >>> from src.preprocessing import enable_mention_cleaning
        >>> enable_mention_cleaning("Halo @user123 apa kabar?")
        "Halo  apa kabar?"
    """
    if not text:
        return text

    return _get_text_cleaner_word().enable_mention_cleaning(text)


def enable_hashtag_cleaning(text: str) -> str:
    """Mengaktifkan pembersihan hashtag pada teks.

    Args:
        text: Teks yang akan dibersihkan

    Returns:
        Teks tanpa hashtag

    Example:
        >>> from src.preprocessing import enable_hashtag_cleaning
        >>> enable_hashtag_cleaning("Hari ini #senin #libur #weekend")
        "Hari ini  "
    """
    if not text:
        return text

    return _get_text_cleaner_word().enable_hashtag_cleaning(text)


def enable_email_cleaning(text: str) -> str:
    """Mengaktifkan pembersihan email pada teks.

    Args:
        text: Teks yang akan dibersihkan

    Returns:
        Teks tanpa email

    Example:
        >>> from src.preprocessing import enable_email_cleaning
        >>> enable_email_cleaning("Kirim email ke test@example.com")
        "Kirim email ke "
    """
    if not text:
        return text

    # Create TextCleanerWord with email cleaning enabled
    cleaner = WordTextCleaner(enable_email_cleaning=True)
    return cleaner.clean_emails(text, keep_text=False)


def enable_phone_cleaning(text: str) -> str:
    """Mengaktifkan pembersihan nomor telepon pada teks.

    Args:
        text: Teks yang akan dibersihkan

    Returns:
        Teks tanpa nomor telepon

    Example:
        >>> from src.preprocessing import enable_phone_cleaning
        >>> enable_phone_cleaning("Hubungi saya di 08123456789")
        "Hubungi saya di "
    """
    if not text:
        return text

    # Create TextCleanerWord with phone cleaning enabled
    cleaner = WordTextCleaner(enable_phone_cleaning=True)
    return cleaner.clean_phones(text, keep_numbers=False)


def enable_currency_cleaning(text: str) -> str:
    """Mengaktifkan pembersihan mata uang pada teks.

    Args:
        text: Teks yang akan dibersihkan

    Returns:
        Teks tanpa mata uang

    Example:
        >>> from src.preprocessing import enable_currency_cleaning
        >>> enable_currency_cleaning("Harga barang adalah $100")
        "Harga barang adalah "
    """
    if not text:
        return text

    # Create TextCleanerWord with currency cleaning enabled
    cleaner = WordTextCleaner(enable_currency_cleaning=True)
    return cleaner.clean_currency(text, keep_numbers=False)


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
            "enable_html_cleaning": globals().get("enable_html_cleaning"),
            "enable_url_cleaning": globals().get("enable_url_cleaning"),
            "enable_mention_cleaning": globals().get("enable_mention_cleaning"),
            "enable_hashtag_cleaning": globals().get("enable_hashtag_cleaning"),
            "enable_email_cleaning": globals().get("enable_email_cleaning"),
            "enable_phone_cleaning": globals().get("enable_phone_cleaning"),
            "enable_currency_cleaning": globals().get("enable_currency_cleaning"),
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
    enable_html_cleaning: bool = False,
    enable_url_cleaning: bool = False,
    enable_mention_cleaning: bool = False,
    enable_hashtag_cleaning: bool = False,
    enable_email_cleaning: bool = False,
    enable_phone_cleaning: bool = False,
    enable_currency_cleaning: bool = False,
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
    if enable_html_cleaning:
        functions.append(globals()["enable_html_cleaning"])
    if enable_url_cleaning:
        functions.append(globals()["enable_url_cleaning"])
    if enable_mention_cleaning:
        functions.append(globals()["enable_mention_cleaning"])
    if enable_hashtag_cleaning:
        functions.append(globals()["enable_hashtag_cleaning"])
    if enable_email_cleaning:
        functions.append(globals()["enable_email_cleaning"])
    if enable_phone_cleaning:
        functions.append(globals()["enable_phone_cleaning"])
    if enable_currency_cleaning:
        functions.append(globals()["enable_currency_cleaning"])

    # Gunakan Pipeline baru untuk proses
    if functions:
        pipe = Pipeline(*functions)
        return pipe.process(text)
    else:
        return text
