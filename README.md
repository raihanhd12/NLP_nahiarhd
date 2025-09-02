# nahiarhdNLP - Indonesian Natural Language Processing Library

Library Indonesian Natural Language Processing dengan fitur preprocessing teks, normalisasi slang, konversi emoji, koreksi ejaan, dan berbagai fungsi text processing lainnya.

## 🚀 Instalasi

```bash
pip install nahiarhdNLP
```

## 📦 Import Library

```python
# Import functions dari preprocessing
from nahiarhdNLP.preprocessing import (
    # Fungsi pembersihan dasar
    remove_html, remove_emoji, remove_url, remove_mentions, remove_hashtags,
    remove_numbers, remove_punctuation, remove_extra_spaces,
    remove_special_chars, remove_whitespace, to_lowercase,
    # Fungsi normalisasi dan koreksi
    replace_spell_corrector, replace_repeated_chars,
    # Fungsi emoji
    emoji_to_words, words_to_emoji,
    # Fungsi linguistic
    remove_stopwords, stem_text, tokenize,
    # Fungsi word-preserving cleaning
    enable_html_cleaning, enable_url_cleaning, enable_mention_cleaning,
    enable_hashtag_cleaning, enable_email_cleaning, enable_phone_cleaning,
    enable_currency_cleaning,
    # Fungsi pipeline
    pipeline, preprocess, Pipeline
)

# Import kelas untuk penggunaan advanced
from nahiarhdNLP.preprocessing import (
    TextCleaner, TextCleanerWord, SpellCorrector, StopwordRemover,
    Stemmer, EmojiConverter, Tokenizer
)

# Import dataset loader
from nahiarhdNLP.datasets import DatasetLoader
```

## 📋 Contoh Penggunaan

### 1. 🧹 TextCleaner - Membersihkan Teks

```python
from nahiarhdNLP.preprocessing import TextCleaner

cleaner = TextCleaner()

# Hapus HTML tags
html_text = "website <a href='https://google.com'>google</a>"
clean_result = cleaner.clean_html(html_text)
print(clean_result)
# Output: "website google"

# Hapus emoji
emoji_text = "Halo dunia 😀😁 apa kabar? 🎉"
clean_result = cleaner.clean_emoji(emoji_text)
print(clean_result)
# Output: "Halo dunia   apa kabar?  "

# Hapus URL
url_text = "kunjungi https://google.com sekarang!"
clean_result = cleaner.clean_urls(url_text)
print(clean_result)
# Output: "kunjungi  sekarang!"

# Hapus mentions
mention_text = "Halo @user123 apa kabar?"
clean_result = cleaner.clean_mentions(mention_text)
print(clean_result)
# Output: "Halo  apa kabar?"

# Hapus Hashtags
hashtag_text = "Hari ini #senin #libur #weekend"
clean_result = cleaner.clean_hashtags(hashtag_text)
print(clean_result)
# Output: "Hari ini  "

# Hapus Angka
number_text = "Saya berumur 25 tahun dan punya 3 anak"
clean_result = cleaner.clean_numbers(number_text)
print(clean_result)
# Output: "Saya berumur  tahun dan punya  anak"

# Hapus Tanda Baca
punct_text = "Halo, apa kabar?! Semoga sehat selalu..."
clean_result = cleaner.clean_punctuation(punct_text)
print(clean_result)
# Output: "Halo apa kabar Semoga sehat selalu"

# Hapus ekstra spasi
space_text = "Halo    dunia   yang    indah"
clean_result = cleaner.clean_extra_spaces(space_text)
print(clean_result)
# Output: "Halo dunia yang indah"

# Hapus karakter khusus
special_text = "Halo @#$%^&*() dunia!!!"
clean_result = cleaner.clean_special_chars(special_text)
print(clean_result)
# Output: "Halo  dunia"

# Hapus spasi
whitespace_text = "Halo\n\tdunia\r\nyang indah"
clean_result = cleaner.clean_whitespace(whitespace_text)
print(clean_result)
# Output: "Halo dunia yang indah"

# Ubah ke huruf kecil
upper_text = "HALO Dunia Yang INDAH"
clean_result = cleaner.to_lowercase(upper_text)
print(clean_result)
# Output: "halo dunia yang indah"
```

### 1.1. ✨ Enable Functions - Pembersihan dengan Mempertahankan Konten

```python
from nahiarhdNLP.preprocessing import TextCleanerWord

cleaner = TextCleanerWord()

# Membersihkan HTML tags
html_text = "Hello <b>world</b>"
clean_result = enable_html_cleaning(html_text)
print(clean_result)
# Output: "Hello world"

# Membersihkan URL
url_text = "Kunjungi https://example.com"
clean_result = enable_url_cleaning(url_text)
print(clean_result)
# Output: "Kunjungi example.com"

# Membersihkan mentions
mention_text = "Halo @user123 apa kabar?"
clean_result = enable_mention_cleaning(mention_text)
print(clean_result)
# Output: "Halo user123 apa kabar?"

# Membersihkan hashtags
hashtag_text = "Hari ini #senin #libur #weekend"
clean_result = enable_hashtag_cleaning(hashtag_text)
print(clean_result)
# Output: "Hari ini senin libur weekend"

# Membersihkan email
email_text = "Kirim email ke test@example.com"
clean_result = enable_email_cleaning(email_text)
print(clean_result)
# Output: "Kirim email ke test example com"

# Membersihkan nomor telepon
phone_text = "Hubungi saya di 08123456789"
clean_result = enable_phone_cleaning(phone_text)
print(clean_result)
# Output: "Hubungi saya di 08123456789"

# Membersihkan mata uang
currency_text = "Harga barang adalah $100"
clean_result = enable_currency_cleaning(currency_text)
print(clean_result)
# Output: "Harga barang adalah 100"
```

### 2. ✏️ SpellCorrector - Koreksi Ejaan & Normalisasi Slang

```python
from nahiarhdNLP.preprocessing import SpellCorrector

spell = SpellCorrector()

# Koreksi kata salah eja
word = "sya"
corrected = spell.correct_word(word)
print(corrected)
# Output: "saya"

# Koreksi kalimat lengkap (termasuk normalisasi slang)
sentence = "sya suka mkn nasi"
corrected = spell.correct_sentence(sentence)
print(corrected)
# Output: "saya suka makan nasi"

# Normalisasi slang
slang_text = "gw lg di rmh"
normalized = spell.correct_sentence(slang_text)
print(normalized)
# Output: "gue lagi di rumah"
```

### 3. 🚫 StopwordRemover - Menghapus Stopwords

```python
from nahiarhdNLP.preprocessing import StopwordRemover

stopword = StopwordRemover()
stopword._load_data()  # Load dataset stopwords

# Menghapus stopwords
text = "saya suka makan nasi goreng"
result = stopword.remove_stopwords(text)
print(result)
# Output: "suka makan nasi goreng"

# Cek apakah kata adalah stopword
is_stop = stopword.is_stopword("adalah")
print(is_stop)  # True
```

### 4. 😀 EmojiConverter - Konversi Emoji

```python
from nahiarhdNLP.preprocessing import EmojiConverter

emoji = EmojiConverter()
emoji._load_data()  # Load dataset emoji

# Emoji ke teks
emoji_text = "😀 😂 😍"
text_result = emoji.emoji_to_text_convert(emoji_text)
print(text_result)
# Output: "wajah_gembira wajah_gembira_berurai_air_mata wajah_tersenyum_lebar_bermata_hati"

# Teks ke emoji
text = "wajah_gembira"
emoji_result = emoji.text_to_emoji_convert(text)
print(emoji_result)
# Output: "😀"
```

### 5. 🔪 Tokenizer - Tokenisasi

```python
from nahiarhdNLP.preprocessing import Tokenizer

tokenizer = Tokenizer()

# Tokenisasi teks
text = "Saya suka makan nasi"
tokens = tokenizer.tokenize(text)
print(tokens)
# Output: ['Saya', 'suka', 'makan', 'nasi']
```

### 6. 🌿 Stemmer - Stemming

```python
from nahiarhdNLP.preprocessing import Stemmer

try:
    stemmer = Stemmer()
    text = "bermain-main dengan senang"
    result = stemmer.stem(text)
    print(result)
    # Output: "main main dengan senang"
except ImportError:
    print("Install Sastrawi dengan: pip install Sastrawi")
```

### 7. 🔀 Pipeline - Preprocessing Sekaligus

Pipeline mendukung **dua cara penggunaan**:

#### A. 🚀 Pipeline dengan Functions (Simple & Clean)

```python
from nahiarhdNLP.preprocessing import Pipeline, remove_html, remove_url, remove_mentions, to_lowercase

# Langsung pass functions yang mau dipakai
pipeline = Pipeline(remove_html, remove_url, remove_mentions)
result = pipeline.process("Hello <b>world</b> @user https://example.com")
print(result)
# Output: "Hello world"

# Bebas pilih functions sesuai kebutuhan
pipeline = Pipeline(remove_url, replace_spell_corrector, to_lowercase)
result = pipeline.process("Halooo https://google.com gw lg nyari info")
print(result)
# Output: "halooo gue lagi mencari info"

# Pipeline bisa dipanggil langsung seperti function
result = pipeline("Test text lainnya")
print(result)

# Contoh untuk social media text
social_pipeline = Pipeline(
    remove_mentions,
    remove_hashtags,
    remove_emoji,
    remove_url,
    replace_spell_corrector,
    to_lowercase
)
result = social_pipeline.process("Halooo @user #trending 😀 https://example.com gw lg nyari info")
print(result)
# Output: "halooo gue lagi mencari info"

# Tokenisasi juga bisa langsung
token_pipeline = Pipeline(remove_url, to_lowercase, tokenize)
tokens = token_pipeline.process("Hello https://google.com World")
print(tokens)  # ['hello', 'world']
```

#### B. 🎯 Pipeline dengan Config Dictionary (Advanced)

```python
from nahiarhdNLP.preprocessing import Pipeline

# Config dictionary untuk kontrol detail
config = {
    "remove_emoji": True,
    "remove_url": True,
    "remove_mentions": True,
    "remove_hashtags": True,
    "remove_numbers": True,
    "replace_spell_corrector": True,
    "to_lowercase": True,
    "remove_punctuation": True,
}

pipeline = Pipeline(config)
result = pipeline.process("Halooo @user123 #trending https://example.com gw lg nyari info pnting 😀!!! 123")
print(result)
# Output: "halo gue lagi mencari info penting 😀!!! 123"

# Pipeline dengan tokenisasi
tokenize_config = {
    "remove_url": True,
    "remove_mentions": True,
    "replace_spell_corrector": True,
    "to_lowercase": True,
    "tokenize": True,
}

pipe = Pipeline(tokenize_config)
result = pipe.process("gw suka makan nasi @user")
print(result)
# Output: ['gue', 'suka', 'makan', 'nasi']

# Advanced features untuk config mode
print("Current config:", pipeline.get_config())
print("Enabled steps:", pipeline.get_enabled_steps())

# Update configuration
pipeline.update_config({"tokenize": True, "remove_stopwords": True})
```

#### C. 🔧 Helper Function pipeline()

```python
from nahiarhdNLP.preprocessing import pipeline

# Preprocessing langsung dengan config
config = {"remove_url": True, "replace_spell_corrector": True, "to_lowercase": True}
result = pipeline("Gw lg browsing https://google.com", config)
print(result)
# Output: "gue lagi rosin"
```

#### 📝 Available Functions untuk Pipeline

```python
# Basic cleaning
remove_html, remove_emoji, remove_url, remove_mentions, remove_hashtags,
remove_numbers, remove_punctuation, remove_special_chars,
remove_whitespace, remove_extra_spaces

# Text transformation
to_lowercase, replace_repeated_chars, replace_spell_corrector

# Emoji handling
emoji_to_words, words_to_emoji

# Linguistic processing
remove_stopwords, stem_text, tokenize

# Word-preserving cleaning
enable_html_cleaning, enable_url_cleaning, enable_mention_cleaning,
enable_hashtag_cleaning, enable_email_cleaning, enable_phone_cleaning,
enable_currency_cleaning
```

### 8. 🎛️ Preprocess Function (Backward Compatibility)

```python
from nahiarhdNLP.preprocessing import preprocess

# Preprocessing dengan parameter eksplisit
result = preprocess(
    "Halooo @user!!! 123 😀",
    remove_emoji=True,
    remove_mentions=True,
    remove_numbers=True,
    remove_punctuation=True,
    replace_repeated_chars=True,
    to_lowercase=True,
    replace_spell_corrector=False,
)
print(result)
# Output: "haloo !! 123"
```

### 9. 📊 Dataset Loader

```python
from nahiarhdNLP.datasets import DatasetLoader

loader = DatasetLoader()

# Load stopwords dari CSV lokal
stopwords = loader.load_stopwords_dataset()
print(f"Jumlah stopwords: {len(stopwords)}")

# Load slang dictionary dari CSV lokal
slang_dict = loader.load_slang_dataset()
print(f"Jumlah slang: {len(slang_dict)}")

# Load emoji dictionary dari CSV lokal
emoji_dict = loader.load_emoji_dataset()
print(f"Jumlah emoji: {len(emoji_dict)}")

# Load wordlist dari JSON lokal
wordlist = loader.load_wordlist_dataset()
print(f"Jumlah kata: {len(wordlist)}")
```

> **Catatan:** Semua dataset (stopword, slang, emoji, wordlist) di-load langsung dari file CSV/JSON di folder `nahiarhdNLP/datasets/`. Tidak ada proses download dari external source.

## 🔥 Demo Script

Untuk melihat semua fitur library bekerja:

```bash
python -m nahiarhdNLP.demo
```

Demo ini menunjukkan:

- ✅ Semua fungsi individual utility
- ✅ Penggunaan class-based approach
- ✅ Pipeline system (functions & config)
- ✅ Advanced pipeline features
- ✅ Handling error dan troubleshooting

## 🚨 Error Handling

```python
try:
    from nahiarhdNLP.preprocessing import SpellCorrector
    spell = SpellCorrector()
    result = spell.correct_sentence("test")
except ImportError:
    print("Package nahiarhdNLP belum terinstall")
    print("Install dengan: pip install nahiarhdNLP")
except Exception as e:
    print(f"Error: {e}")
```

## 💡 Tips Penggunaan

1. **Untuk preprocessing simple**: Gunakan `Pipeline(function1, function2, ...)` - langsung pass functions!
2. **Untuk kontrol detail**: Gunakan `Pipeline(config_dict)` atau `preprocess()` dengan parameter boolean
3. **Untuk kontrol penuh**: Gunakan kelas individual (`TextCleaner`, `SpellCorrector`, dll)
4. **Untuk spell correction + slang**: Gunakan `SpellCorrector` yang menggabungkan kedua fitur
5. **Untuk menghapus emoji**: Gunakan `remove_emoji()` atau set `remove_emoji=True` di Pipeline/preprocess
6. **Untuk stemming**: Install Sastrawi terlebih dahulu: `pip install Sastrawi`
7. **Untuk load dataset**: Gunakan `DatasetLoader` dari `nahiarhdNLP.datasets`
8. **Untuk inisialisasi kelas**: Panggil `_load_data()` untuk kelas yang memerlukan dataset
9. **Pipeline design**: `Pipeline(remove_url, to_lowercase)` lebih jelas daripada config dictionary
10. **Function chaining**: Pipeline bisa dipanggil seperti function dengan `pipeline("text")`
11. **Demo testing**: Jalankan `python -m nahiarhdNLP.demo` untuk melihat semua fitur bekerja

## ⚡ Performance & Dataset

nahiarhdNLP menggunakan **dataset lokal** yang sudah disediakan:

- **Stopwords**: File `stop_word.csv` (788 kata)
- **Slang Dictionary**: File `slang.csv` (15,675 pasangan)
- **Emoji Mapping**: File `emoji.csv` (3,530 emoji)
- **Wordlist**: File `wordlist.json` (kamus kata Indonesia)
- **KBBI Dictionary**: File `kata_dasar_kbbi.csv` (28,527 kata)
- **Kamus Tambahan**: File `kamus.txt` (30,871 kata)

Semua dataset tersimpan di folder `nahiarhdNLP/datasets/` dan diakses melalui `DatasetLoader`.

## 📦 Dependencies

Package ini membutuhkan:

- `pandas` - untuk load dan proses dataset CSV/JSON
- `Sastrawi` - untuk stemming (opsional)
- `rich` - untuk output formatting di demo (opsional)

## 🔧 Struktur Modul

```text
nahiarhdNLP/
├── datasets/
│   ├── loaders.py          # DatasetLoader class
│   ├── emoji.csv           # Dataset emoji (3,530 entries)
│   ├── slang.csv           # Dataset slang (15,675 entries)
│   ├── stop_word.csv       # Dataset stopwords (788 entries)
│   ├── wordlist.json       # Dataset wordlist
│   ├── kata_dasar_kbbi.csv # Dataset KBBI (28,527 entries)
│   └── kamus.txt           # Dataset kamus tambahan (30,871 entries)
├── preprocessing/
│   ├── cleaning/
│   │   ├── text_cleaner.py     # TextCleaner class (complete removal)
│   │   └── text_cleaner_word.py # Word-preserving TextCleaner class
│   ├── linguistic/
│   │   ├── stemmer.py      # Stemmer class
│   │   └── stopwords.py    # StopwordRemover class
│   ├── normalization/
│   │   ├── emoji.py        # EmojiConverter class
│   │   └── spell_corrector.py # SpellCorrector class
│   ├── tokenization/
│   │   └── tokenizer.py    # Tokenizer class
│   └── utils.py            # Fungsi utility individual & Pipeline
└── demo.py                 # File demo penggunaan
```

## 🆕 Changelog Versi 1.4.0

- 🚀 **[FITUR BARU]** Menambahkan `remove_emoji()` function untuk menghapus emoji dari teks
- ✅ **[BARU]** TextCleaner sekarang memiliki method `clean_emoji()` untuk menghapus emoji
- ✅ **[BARU]** Pipeline mendukung "remove_emoji" config untuk emoji removal
- ✅ **[BARU]** Preprocess function mendukung parameter `remove_emoji=True/False`
- ✅ **[PERBAIKAN]** Demo script diperbarui dengan contoh emoji removal
- ✅ **[PERBAIKAN]** Dokumentasi lengkap untuk fitur emoji removal
- 🚀 **[MAJOR]** Pipeline sekarang mendukung 2 mode: Functions dan Config Dictionary
- ✅ **[BARU]** Pipeline dengan functions: `Pipeline(remove_url, to_lowercase)`
- ✅ **[BARU]** Pipeline dengan config: `Pipeline({"remove_url": True, "to_lowercase": True})`
- ✅ **[BARU]** Advanced pipeline features: `get_config()`, `get_enabled_steps()`, `update_config()`
- ✅ **[PERBAIKAN]** Fungsi `pipeline(text, config)` sekarang bekerja dengan config dictionary
- ✅ **[PERBAIKAN]** TextCleaner sekarang punya method `clean_html()` yang benar
- ✅ **[PERBAIKAN]** SpellCorrector demo diperbaiki dengan proper instantiation
- ✅ **[PERBAIKAN]** Demo script berjalan sempurna tanpa error
- ✅ **[PERBAIKAN]** Dokumentasi yang akurat dan sesuai implementasi
- ✅ **[PERBAIKAN]** Function names yang konsisten: `replace_spell_corrector`, `replace_repeated_chars`
- ✅ **[PERBAIKAN]** Backward compatibility dengan `preprocess()` function
- ✅ Menggabungkan spell correction dan slang normalization dalam `SpellCorrector`
- ✅ Semua dataset menggunakan file lokal (CSV/JSON)
- ✅ Struktur yang lebih terorganisir dengan pemisahan kelas dan fungsi
- ✅ Penambahan `DatasetLoader` untuk manajemen dataset terpusat
- ✅ Dataset lengkap dengan 6 file berbeda (emoji, slang, stopwords, wordlist, KBBI, kamus)

## 🆕 Changelog Versi 1.4.4 (Latest)

- 🚀 **[FITUR BARU]** Enable Functions untuk pembersihan dengan mempertahankan konten
- ✅ **[BARU]** `enable_html_cleaning()` - Membersihkan HTML tags
- ✅ **[BARU]** `enable_url_cleaning()` - Membersihkan URL
- ✅ **[BARU]** `enable_mention_cleaning()` - Membersihkan mentions (@user)
- ✅ **[BARU]** `enable_hashtag_cleaning()` - Membersihkan hashtags (#tag)
- ✅ **[BARU]** `enable_email_cleaning()` - Membersihkan email
- ✅ **[BARU]** `enable_phone_cleaning()` - Membersihkan nomor telepon
- ✅ **[BARU]** `enable_currency_cleaning()` - Membersihkan mata uang
- ✅ **[BARU]** Demo script diperbarui dengan contoh lengkap untuk semua fitur baru
- ✅ **[BARU]** Dokumentasi README lengkap dengan contoh penggunaan fitur baru
- ✅ **[PERBAIKAN]** Integrasi penuh dengan sistem Pipeline dan preprocess functions
- ✅ **[PERBAIKAN]** Backward compatibility dengan semua fitur existing
- ✅ **[PERBAIKAN]** Package structure yang konsisten dan terorganisir

## 🐛 Troubleshooting

**Error saat import dataset:**

```python
# Pastikan memanggil _load_data() untuk kelas yang memerlukan dataset
stopword = StopwordRemover()
stopword._load_data()  # Penting!
```

**Error Sastrawi tidak ditemukan:**

```bash
pip install Sastrawi
```

**Error pandas tidak ditemukan:**

```bash
pip install pandas
```

**Testing semua fitur:**

```bash
python -m nahiarhdNLP.demo
```

## 📄 License

MIT License

## 👨‍💻 Author

Raihan Hidayatullah Djunaedi [raihanhd.dev@gmail.com](mailto:raihanhd.dev@gmail.com)

---

Untuk contoh penggunaan lengkap, lihat file `demo.py` di repository ini atau jalankan `python -m nahiarhdNLP.demo`.
