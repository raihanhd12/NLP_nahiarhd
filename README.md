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
    # Fungsi word-preserving cleaning (BARU!)
    clean_emails_preserve_text, clean_phones_preserve_numbers, clean_currency_preserve_numbers,
    clean_urls_preserve_domain, clean_mentions_preserve_username, clean_hashtags_preserve_tags,
    clean_html_preserve_content, clean_all_preserve_words,
    # Fungsi pipeline
    pipeline, preprocess, Pipeline
)

# Import kelas untuk penggunaan advanced
from nahiarhdNLP.preprocessing import (
    TextCleaner, SpellCorrector, StopwordRemover,
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

# Membersihkan HTML tags
html_text = "website <a href='https://google.com'>google</a>"
clean_result = cleaner.clean_html(html_text)
print(clean_result)
# Output: "website google"

# Membersihkan URL
url_text = "kunjungi https://google.com sekarang!"
clean_result = cleaner.clean_urls(url_text)
print(clean_result)
# Output: "kunjungi sekarang!"

# Membersihkan mentions
mention_text = "Halo @user123 apa kabar?"
clean_result = cleaner.clean_mentions(mention_text)
print(clean_result)
# Output: "Halo apa kabar?"

# Membersihkan emoji
emoji_text = "Halo dunia 😀😁 apa kabar? 🎉"
clean_result = cleaner.clean_emoji(emoji_text)
print(clean_result)
# Output: "Halo dunia apa kabar?"
```

### 1.5. 🛡️ Word-Preserving TextCleaner - Membersihkan Teks dengan Mempertahankan Konten (BARU!)

```python
from nahiarhdNLP.preprocessing import TextCleaner

# Buat TextCleaner dengan opsi word-preserving
cleaner = TextCleaner(
    remove_urls=True,
    remove_mentions=True,
    remove_hashtags=True,
    clean_emails=True,      # BARU!
    clean_phones=True,      # BARU!
    clean_currency=True     # BARU!
)

# Membersihkan URL tapi tetap mempertahankan domain
url_text = "kunjungi https://google.com sekarang!"
clean_result = cleaner.clean_urls(url_text)
print(clean_result)
# Output: "kunjungi google sekarang!"

# Membersihkan mentions tapi tetap mempertahankan username
mention_text = "Halo @user123 apa kabar?"
clean_result = cleaner.clean_mentions(mention_text)
print(clean_result)
# Output: "Halo user123 apa kabar?"

# Membersihkan hashtags tapi tetap mempertahankan tag
hashtag_text = "Hari ini #senin #libur #weekend"
clean_result = cleaner.clean_hashtags(hashtag_text)
print(clean_result)
# Output: "Hari ini senin libur weekend"

# 🆕 BARU: Membersihkan email tapi tetap mempertahankan teks
email_text = "Contact me at john.doe@gmail.com"
clean_result = cleaner.clean_emails(email_text)
print(clean_result)
# Output: "Contact me at john doe gmail com"

# 🆕 BARU: Membersihkan nomor telepon tapi tetap mempertahankan angka
phone_text = "Call me at (555) 123-4567"
clean_result = cleaner.clean_phones(phone_text)
print(clean_result)
# Output: "Call me at 5551234567"

# 🆕 BARU: Membersihkan simbol mata uang tapi tetap mempertahankan angka
currency_text = "The price is $100.50 and €75.25"
clean_result = cleaner.clean_currency(currency_text)
print(clean_result)
# Output: "The price is 100.50 and 75.25"

# Atau gunakan fungsi individual untuk kemudahan
from nahiarhdNLP.preprocessing import (
    clean_emails_preserve_text,
    clean_phones_preserve_numbers,
    clean_currency_preserve_numbers
)

# Fungsi individual untuk email
email_result = clean_emails_preserve_text("Contact john.doe@gmail.com")
print(email_result)
# Output: "Contact john doe gmail com"

# Fungsi individual untuk telepon
phone_result = clean_phones_preserve_numbers("Call (555) 123-4567")
print(phone_result)
# Output: "Call 5551234567"

# Fungsi individual untuk mata uang
currency_result = clean_currency_preserve_numbers("Price: $99.99")
print(currency_result)
# Output: "Price: 99.99"

# Clean semua sekaligus dengan mempertahankan konten
from nahiarhdNLP.preprocessing import clean_all_preserve_words

mixed_text = "Hello @user! Check #cars at https://google.com, contact john@gmail.com, call (555)123-4567, price $100"
result = clean_all_preserve_words(mixed_text, clean_emails=True, clean_phones=True, clean_currency=True)
print(result)
# Output: "Hello user! Check cars at google, contact john gmail com, call 5551234567, price 100"
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

### 7. 🛠️ Fungsi Individual

```python
from nahiarhdNLP.preprocessing import (
    remove_html, remove_emoji, remove_url, remove_mentions, remove_hashtags,
    remove_numbers, remove_punctuation, remove_extra_spaces,
    remove_special_chars, remove_whitespace, to_lowercase,
    replace_spell_corrector, replace_repeated_chars,
    emoji_to_words, words_to_emoji, remove_stopwords,
    stem_text, tokenize,
    # 🆕 BARU: Word-preserving cleaning functions
    clean_emails_preserve_text, clean_phones_preserve_numbers, clean_currency_preserve_numbers,
    clean_urls_preserve_domain, clean_mentions_preserve_username, clean_hashtags_preserve_tags,
    clean_html_preserve_content, clean_all_preserve_words
)

# 🧹 FUNGSI PEMBERSIHAN DASAR

# Menghapus HTML tags
html_text = "website <a href='https://google.com'>google</a>"
clean_result = remove_html(html_text)
print(clean_result)
# Output: "website google"

# Menghapus emoji
emoji_text = "Halo dunia 😀😁 apa kabar? 🎉"
clean_result = remove_emoji(emoji_text)
print(clean_result)
# Output: "Halo dunia apa kabar?"

# Menghapus URL
url_text = "kunjungi https://google.com sekarang!"
clean_result = remove_url(url_text)
print(clean_result)
# Output: "kunjungi sekarang!"

# Menghapus mentions (@username)
mention_text = "Halo @user123 dan @admin apa kabar?"
clean_result = remove_mentions(mention_text)
print(clean_result)
# Output: "Halo dan apa kabar?"

# Menghapus hashtags (#tag)
hashtag_text = "Hari ini #senin #libur #weekend"
clean_result = remove_hashtags(hashtag_text)
print(clean_result)
# Output: "Hari ini"

# ✨ FUNGSI NORMALISASI DAN KOREKSI

# Normalisasi slang dan koreksi ejaan
slang_text = "emg siapa yg nanya?"
normal_text = replace_spell_corrector(slang_text)
print(normal_text)
# Output: "memang siapa yang bertanya?"

# Mengatasi perpanjangan kata (word elongation)
elongation_text = "kenapaaa???"
clean_result = replace_repeated_chars(elongation_text)
print(clean_result)
# Output: "kenapaa??"

# 😀 FUNGSI EMOJI

# Konversi emoji ke kata
emoji_text = "emoji 😀😁"
text_result = emoji_to_words(emoji_text)
print(text_result)
# Output: "emoji wajah_gembira wajah_gembira_dengan_mata_bahagia"

# Konversi kata ke emoji
text_to_emoji = "emoji wajah_gembira"
emoji_result = words_to_emoji(text_to_emoji)
print(emoji_result)
# Output: "emoji 😀"

# 🆕 BARU: WORD-PRESERVING CLEANING FUNCTIONS

# Membersihkan URL tapi tetap mempertahankan domain
url_text = "kunjungi https://google.com sekarang!"
clean_result = clean_urls_preserve_domain(url_text)
print(clean_result)
# Output: "kunjungi google sekarang!"

# Membersihkan mentions tapi tetap mempertahankan username
mention_text = "Halo @user123 apa kabar?"
clean_result = clean_mentions_preserve_username(mention_text)
print(clean_result)
# Output: "Halo user123 apa kabar?"

# Membersihkan hashtags tapi tetap mempertahankan tag
hashtag_text = "Hari ini #senin #libur #weekend"
clean_result = clean_hashtags_preserve_tags(hashtag_text)
print(clean_result)
# Output: "Hari ini senin libur weekend"

# Membersihkan HTML tapi tetap mempertahankan konten
html_text = "website <a href='https://google.com'>google</a>"
clean_result = clean_html_preserve_content(html_text)
print(clean_result)
# Output: "website google"

# 🆕 Membersihkan email tapi tetap mempertahankan teks
email_text = "Contact me at john.doe@gmail.com"
clean_result = clean_emails_preserve_text(email_text)
print(clean_result)
# Output: "Contact me at john doe gmail com"

# 🆕 Membersihkan nomor telepon tapi tetap mempertahankan angka
phone_text = "Call me at (555) 123-4567"
clean_result = clean_phones_preserve_numbers(phone_text)
print(clean_result)
# Output: "Call me at 5551234567"

# 🆕 Membersihkan simbol mata uang tapi tetap mempertahankan angka
currency_text = "The price is $100.50 and €75.25"
clean_result = clean_currency_preserve_numbers(currency_text)
print(clean_result)
# Output: "The price is 100.50 and 75.25"

# 🔬 FUNGSI LINGUISTIC

# Menghapus stopwords
stopword_text = "siapa yang suruh makan?!!"
clean_result = remove_stopwords(stopword_text)
print(clean_result)
# Output: "suruh makan?!!"

# Stemming teks (memerlukan Sastrawi)
try:
    stem_text_input = "bermain-main dengan senang"
    stemmed = stem_text(stem_text_input)
    print(stemmed)
    # Output: "main main dengan senang"
except ImportError:
    print("Install Sastrawi: pip install Sastrawi")

# Tokenisasi teks
tokenize_text = "Saya suka makan nasi"
tokens = tokenize(tokenize_text)
print(tokens)
# Output: ['Saya', 'suka', 'makan', 'nasi']
```

### 8. 🔀 Pipeline - Preprocessing Sekaligus

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
```

### 9. 🎛️ Preprocess Function (Backward Compatibility)

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

### 10. 📊 Dataset Loader

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
│   │   └── text_cleaner_word.py # Word-preserving TextCleaner class (BARU!)
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

## 🆕 Changelog Versi 1.5.0

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

## 🆕 Changelog Versi 1.6.0 (Latest)

- 🚀 **[FITUR BARU]** Word-Preserving Text Cleaning System
- ✅ **[BARU]** `TextCleaner` class dengan opsi word-preserving untuk mempertahankan konten berharga
- ✅ **[BARU]** Method `clean_emails()` - Membersihkan email tapi tetap mempertahankan teks (`john.doe@gmail.com` → `john doe gmail com`)
- ✅ **[BARU]** Method `clean_phones()` - Membersihkan nomor telepon tapi tetap mempertahankan angka ((555)123-4567 → 5551234567)
- ✅ **[BARU]** Method `clean_currency()` - Membersihkan simbol mata uang tapi tetap mempertahankan angka ($100.50 → 100.50)
- ✅ **[BARU]** Fungsi utility individual: `clean_emails_preserve_text()`, `clean_phones_preserve_numbers()`, `clean_currency_preserve_numbers()`
- ✅ **[BARU]** Fungsi `clean_all_preserve_words()` untuk cleaning komprehensif dengan mempertahankan konten
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
