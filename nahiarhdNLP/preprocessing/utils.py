"""
Utility functions for preprocessing Indonesian text.
"""

import re
from typing import Callable, List

from .cleaning.spell_corrector import SpellCorrector

# Import kelas-kelas yang sudah ada
from .cleaning.text_cleaner import TextCleaner
from .linguistic.stemmer import Stemmer
from .linguistic.stopwords import StopwordRemover
from .normalization.emoji import EmojiConverter
from .normalization.slang import SlangNormalizer
from .tokenization.tokenizer import Tokenizer

# Inisialisasi instance global untuk fungsi-fungsi utility (lazy loading)
_text_cleaner = None
_stopword_remover = None
_slang_normalizer = None
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


def _get_slang_normalizer():
    global _slang_normalizer
    if _slang_normalizer is None:
        _slang_normalizer = SlangNormalizer()
        _slang_normalizer._load_data()
    return _slang_normalizer


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

    # Pattern untuk menghapus HTML tags
    html_pattern = r"<[^>]+>"
    result = re.sub(html_pattern, "", text)

    # Bersihkan spasi berlebih
    result = re.sub(r"\s+", " ", result).strip()

    return result


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

    return _get_text_cleaner().clean_urls(text)


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


def replace_slang(text: str) -> str:
    """Mengganti kata gaul (slang) menjadi kata formal.

    Args:
        text: Teks yang mengandung kata slang

    Returns:
        Teks dengan kata formal

    Example:
        >>> from src.preprocessing import replace_slang
        >>> replace_slang("emg siapa yg nanya?")
        "memang siapa yang bertanya?"
    """
    if not text:
        return text

    return _get_slang_normalizer().normalize(text)


def replace_word_elongation(text: str) -> str:
    """Mengatasi word elongation (karakter berulang).

    Args:
        text: Teks dengan karakter berulang

    Returns:
        Teks dengan karakter berulang dinormalisasi

    Example:
        >>> from src.preprocessing import replace_word_elongation
        >>> replace_word_elongation("kenapaaa?")
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

    # Pattern untuk mentions
    mention_pattern = r"@\w+"
    result = re.sub(mention_pattern, "", text)

    # Bersihkan spasi berlebih
    result = re.sub(r"\s+", " ", result).strip()

    return result


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

    # Pattern untuk hashtags
    hashtag_pattern = r"#\w+"
    result = re.sub(hashtag_pattern, "", text)

    # Bersihkan spasi berlebih
    result = re.sub(r"\s+", " ", result).strip()

    return result


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

    # Pattern untuk numbers
    number_pattern = r"\d+"
    result = re.sub(number_pattern, "", text)

    # Bersihkan spasi berlebih
    result = re.sub(r"\s+", " ", result).strip()

    return result


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

    # Pattern untuk punctuation
    punctuation_pattern = r"[^\w\s]"
    result = re.sub(punctuation_pattern, "", text)

    # Bersihkan spasi berlebih
    result = re.sub(r"\s+", " ", result).strip()

    return result


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

    # Replace multiple spaces with single space
    result = re.sub(r"\s+", " ", text)
    return result.strip()


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

    # Keep alphanumeric, spaces, and common punctuation
    special_pattern = r'[^\w\s.,!?;:()"\'-]'
    result = re.sub(special_pattern, "", text)

    # Bersihkan spasi berlebih
    result = re.sub(r"\s+", " ", result).strip()

    return result


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

    # Replace tabs, newlines, etc. with spaces
    result = re.sub(r"\t", " ", text)
    result = re.sub(r"\n", " ", text)
    result = re.sub(r"\r", " ", text)

    # Bersihkan spasi berlebih
    result = re.sub(r"\s+", " ", result).strip()

    return result


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

    return text.lower()


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


def correct_spelling(text: str) -> str:
    """Mengoreksi ejaan kata dalam teks.

    Args:
        text: Teks yang mungkin mengandung kata salah eja

    Returns:
        Teks dengan ejaan dikoreksi

    Example:
        >>> from src.preprocessing import correct_spelling
        >>> correct_spelling("sya suka mkn nasi")
        "saya suka makan nasi"
    """
    if not text:
        return text

    return _get_spell_corrector().correct_sentence(text)


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

    global _stemmer
    if _stemmer is None:
        _stemmer = Stemmer()

    return _stemmer.stem(text)


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


def clean_text(text: str) -> str:
    """Membersihkan teks secara menyeluruh.

    Args:
        text: Teks yang akan dibersihkan

    Returns:
        Teks yang sudah dibersihkan

    Example:
        >>> from src.preprocessing import clean_text
        >>> clean_text("Halooo!!! @user #trending https://example.com 😀")
        "halo"
    """
    if not text:
        return text

    return _get_text_cleaner().clean(text)


def pipeline(functions: List[Callable[[str], str]]) -> Callable[[str], str]:
    """Membuat pipeline dari sequence fungsi preprocessing.

    Args:
        functions: List fungsi preprocessing yang akan dijalankan secara berurutan

    Returns:
        Fungsi pipeline yang dapat digunakan untuk memproses teks

    Example:
        >>> from src.preprocessing import pipeline, replace_word_elongation, replace_slang
        >>> pipe = pipeline([replace_word_elongation, replace_slang])
        >>> pipe("Knp emg gk mw makan kenapaaa???")
        "mengapa memang tidak mau makan mengapa???"
    """

    def process_text(text: str) -> str:
        """Memproses teks melalui semua fungsi dalam pipeline."""
        if not text:
            return text

        result = text
        for func in functions:
            result = func(result)

        return result

    return process_text


def preprocess(
    text: str,
    remove_html_tags: bool = True,
    remove_urls: bool = True,
    remove_stopwords_flag: bool = True,
    replace_slang_flag: bool = True,
    replace_elongation: bool = True,
    convert_emoji: bool = True,
    correct_spelling_flag: bool = False,
    stem_text_flag: bool = False,
    to_lowercase: bool = True,
) -> str:
    """Fungsi preprocessing all-in-one dengan berbagai opsi.

    Args:
        text: Teks yang akan diproses
        remove_html_tags: Apakah menghapus HTML tags
        remove_urls: Apakah menghapus URL
        remove_stopwords_flag: Apakah menghapus stopwords
        replace_slang_flag: Apakah mengganti slang
        replace_elongation: Apakah mengatasi word elongation
        convert_emoji: Apakah mengubah emoji ke kata
        correct_spelling_flag: Apakah mengoreksi ejaan
        stem_text_flag: Apakah melakukan stemming
        to_lowercase: Apakah mengubah ke lowercase

    Returns:
        Teks yang sudah diproses

    Example:
        >>> from src.preprocessing import preprocess
        >>> preprocess("Halooo emg siapa yg nanya? 😀")
        "halo memang siapa yang bertanya wajah_gembira"
    """
    if not text:
        return text

    result = text

    # Bersihkan HTML tags
    if remove_html_tags:
        result = remove_html(result)

    # Bersihkan URL
    if remove_urls:
        result = remove_url(result)

    # Atasi word elongation
    if replace_elongation:
        result = replace_word_elongation(result)

    # Ubah emoji ke kata
    if convert_emoji:
        result = emoji_to_words(result)

    # Ganti slang
    if replace_slang_flag:
        result = replace_slang(result)

    # Koreksi ejaan (opsional karena lambat)
    if correct_spelling_flag:
        result = correct_spelling(result)

    # Hapus stopwords
    if remove_stopwords_flag:
        result = remove_stopwords(result)

    # Stemming (opsional)
    if stem_text_flag:
        result = stem_text(result)

    # Lowercase
    if to_lowercase:
        result = result.lower()

    # Bersihkan spasi berlebih
    result = re.sub(r"\s+", " ", result).strip()

    return result
