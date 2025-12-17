# nahiarhdNLP — Indonesian NLP utilities

Lightweight utilities for Indonesian text preprocessing: cleaning, normalization, emoji conversion, spell correction, stemming, stopwords and a configurable Pipeline.

## Install

```bash
pip install nahiarhdNLP
```

## Quick usage

Import the pipeline and helpers:

```python
from nahiarhdNLP.preprocessing import Pipeline, pipeline
from nahiarhdNLP.preprocessing import remove_html, remove_mentions, to_lowercase
```

1. Pipeline with callables (function mode):

```python
pipe = Pipeline(remove_html, remove_mentions, to_lowercase)
result = pipe.process("Hello <b>WORLD</b> @user https://example.com")
# -> HTML removed, mentions cleaned, lowered
```

2. Pipeline with config dictionary (config mode):

```python
config = {"clean_html": True, "clean_mentions": True, "remove_urls": True}
pipe = Pipeline(config)
result = pipe.process("Hello <b>World</b> @User https://EXAMPLE.com")
```

3. Helper `pipeline()` for one-shot processing with a config:

```python
result = pipeline("Gw lg browsing https://google.com", {"remove_urls": True, "to_lowercase": True})
```

## Running tests (local)

Project contains unit tests under `nahiarhdNLP/tests`. To run them locally in the project virtualenv:

```bash
# from project root
# ensure virtualenv is active, or install pytest into your environment
python3 -m pip install -U "pytest" "pytest-cov"
python3 -m pytest -q
```

If you use the project `.venv`, run:

```bash
.venv/bin/python3 -m pip install -U pytest pytest-cov
.venv/bin/python3 -m pytest -q
```

## Notes & troubleshooting

- The package exposes two pipeline implementations:
  - `nahiarhdNLP.preprocessing.main.Pipeline` (config-only implementation) — useful for config-driven workflows.
  - `nahiarhdNLP.preprocessing.utils.Pipeline` (function-or-config implementation) — supports both passing callables and config dicts.
- If you see import-time errors, ensure the package root is on `PYTHONPATH` or install the package in editable mode:

```bash
pip install -e .
```

If you want more examples (tokenization, stemmer, emoji conversion, or spell-correction examples), tell me which features you want documented and I'll add them to this README.

## More examples

### Stemmer

```python
from nahiarhdNLP.preprocessing import Stemmer

try:
    stemmer = Stemmer()
    text = "bermain-main dengan senang"
    stemmed = stemmer.stem(text)
    print(stemmed)
    # Expected: "main main dengan senang"
except Exception as e:
    print("Stemmer error:", e)
    print("Install Sastrawi if missing: pip install Sastrawi")
```

### EmojiConverter

```python
from nahiarhdNLP.preprocessing import EmojiConverter

emoji = EmojiConverter()
emoji._load_data()
print(emoji.emoji_to_text_convert("😀😁"))
# e.g. -> "wajah_gembira wajah_menyeringai"
print(emoji.text_to_emoji_convert("wajah_gembira"))
# e.g. -> "😀"
```

### SpellCorrector (slang + spelling)

```python
from nahiarhdNLP.preprocessing import SpellCorrector

spell = SpellCorrector()
print(spell.correct_word("sya"))
# e.g. -> "saya"
print(spell.correct_sentence("gw lg di rmh"))
# e.g. -> "gue lagi di rumah"
```

# Linguistic processing

remove_stopwords, stem_text, tokenize

# Word-preserving cleaning

enable_html_cleaning, enable_url_cleaning, enable_mention_cleaning,
enable_hashtag_cleaning, enable_email_cleaning, enable_phone_cleaning,
enable_currency_cleaning

# Replacement helpers (new)

replace_email, replace_link, replace_user

````

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
````

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

## 🆕 Changelog Versi 1.4.11 (Latest)

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
