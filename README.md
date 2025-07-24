# nahiarhdNLP - Advanced Indonesian Natural Language Processing Library

Advanced Indonesian Natural Language Processing Library dengan fitur preprocessing teks, normalisasi slang, konversi emoji, koreksi ejaan, dan banyak lagi.

## 🚀 Instalasi

```bash
pip install nahiarhdNLP
```

## 📦 Import Library

```python
# Import module preprocessing
from nahiarhdNLP import preprocessing

# Import fungsi spesifik
from nahiarhdNLP.preprocessing import (
    remove_html, remove_url, remove_mentions, replace_slang,
    emoji_to_words, correct_spelling, clean_text
)

# Import kelas untuk penggunaan advanced
from nahiarhdNLP.preprocessing import (
    TextCleaner, SpellCorrector, StopwordRemover,
    Stemmer, EmojiConverter, Tokenizer
)

# Import dataset loader (dua cara)
from nahiarhdNLP.datasets import DatasetLoader
# atau
from nahiarhdNLP.datasets.loaders import DatasetLoader
```

## 📋 Contoh Penggunaan

### 1. 🧹 TextCleaner - Membersihkan Teks

```python
from nahiarhdNLP.preprocessing import TextCleaner

cleaner = TextCleaner()

# Membersihkan URL
url_text = "kunjungi https://google.com sekarang!"
clean_result = cleaner.clean_urls(url_text)
print(clean_result)
# Output: "kunjungi  sekarang!"

# Membersihkan mentions
mention_text = "Halo @user123 apa kabar?"
clean_result = cleaner.clean_mentions(mention_text)
print(clean_result)
# Output: "Halo  apa kabar?"

# Membersihkan teks secara menyeluruh
messy_text = "Halooo!!! @user #trending https://example.com 😀"
clean_result = cleaner.clean(messy_text)
print(clean_result)
# Output: teks yang sudah dibersihkan
```

### 2. ✏️ SpellCorrector - Koreksi Ejaan & Normalisasi Slang

```python
from nahiarhdNLP.preprocessing import SpellCorrector

spell = SpellCorrector()

# Koreksi kata salah eja
word = "mencri"
corrected = spell.correct_word(word)
print(corrected)
# Output: "mencuri"

# Koreksi kalimat lengkap (termasuk normalisasi slang)
sentence = "gw lg mencri informsi"
corrected = spell.correct_sentence(sentence)
print(corrected)
# Output: "saya lagi mencuri informasi"
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

# Menambah custom stopwords
stopword.add_custom_stopwords(["adalah", "akan"])
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
# Output: "wajah_gembira wajah_tertawa wajah_bercinta"

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
text = "ini contoh tokenisasi"
tokens = tokenizer.tokenize(text)
print(tokens)
# Output: ['ini', 'contoh', 'tokenisasi']
```

### 6. 🌿 Stemmer - Stemming (Memerlukan Sastrawi)

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
    remove_html, remove_url, remove_mentions,
    replace_slang, emoji_to_words, correct_spelling,
    remove_stopwords, clean_text
)

# Menghapus HTML
html_text = "website <a href='https://google.com'>google</a>"
clean_text_result = remove_html(html_text)
print(clean_text_result)
# Output: "website google"

# Menghapus URL
url_text = "kunjungi https://google.com sekarang!"
clean_text_result = remove_url(url_text)
print(clean_text_result)
# Output: "kunjungi  sekarang!"

# Normalisasi slang (menggunakan SpellCorrector)
slang_text = "emg siapa yg nanya?"
normal_text = replace_slang(slang_text)
print(normal_text)
# Output: "memang siapa yang bertanya?"

# Konversi emoji
emoji_text = "😀 😂 😍"
text_result = emoji_to_words(emoji_text)
print(text_result)
# Output: "wajah_gembira wajah_tertawa wajah_bercinta"

# Koreksi ejaan
spell_text = "saya mencri informsi"
corrected = correct_spelling(spell_text)
print(corrected)
# Output: "saya mencuri informasi"

# Cleaning menyeluruh
messy_text = "Halooo!!! @user #trending https://example.com"
cleaned = clean_text(messy_text)
print(cleaned)
# Output: teks yang sudah dibersihkan
```

### 8. 📊 Dataset Loader

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

> **Catatan:** Semua dataset (stopword, slang, emoji, wordlist) di-load langsung dari file CSV/JSON di folder `nahiarhdNLP/datasets/`. Tidak ada proses cache atau download dari HuggingFace.

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

1. **Untuk cleaning dasar**: Gunakan `clean_text()` atau kelas `TextCleaner`
2. **Untuk kontrol penuh**: Gunakan kelas individual (`TextCleaner`, `SpellCorrector`, dll)
3. **Untuk spell correction + slang**: Gunakan `SpellCorrector` yang menggabungkan kedua fitur
4. **Untuk stemming**: Install Sastrawi terlebih dahulu: `pip install Sastrawi`
5. **Untuk load dataset**: Gunakan `DatasetLoader` dari `nahiarhdNLP.datasets`
6. **Untuk inisialisasi kelas**: Jangan lupa panggil `_load_data()` untuk kelas yang memerlukan dataset

## ⚡ Performance & Dataset

Mulai versi terbaru, nahiarhdNLP **menggunakan dataset lokal** yang sudah disediakan:

- **Stopwords**: File `stop_word.csv`
- **Slang Dictionary**: File `slang.csv`
- **Emoji Mapping**: File `emoji.csv`
- **Wordlist**: File `wordlist.json`
- **KBBI Dictionary**: File `kata_dasar_kbbi.csv`

Semua dataset tersimpan di folder `nahiarhdNLP/datasets/` dan diakses melalui `DatasetLoader`.

## 📦 Dependencies

Package ini membutuhkan:

- `pandas` - untuk load dan proses dataset CSV/JSON
- `sastrawi` - untuk stemming (opsional)
- `rich` - untuk output formatting (opsional)

## 🔧 Struktur Modul

```
nahiarhdNLP/
├── datasets/
│   ├── loaders.py          # DatasetLoader class
│   ├── emoji.csv           # Dataset emoji
│   ├── slang.csv           # Dataset slang
│   ├── stop_word.csv       # Dataset stopwords
│   ├── wordlist.json       # Dataset wordlist
│   └── kata_dasar_kbbi.csv # Dataset KBBI
├── preprocessing/
│   ├── cleaning/
│   │   └── text_cleaner.py # TextCleaner class
│   ├── linguistic/
│   │   ├── stemmer.py      # Stemmer class
│   │   └── stopwords.py    # StopwordRemover class
│   ├── normalization/
│   │   ├── emoji.py        # EmojiConverter class
│   │   └── spell_corrector.py # SpellCorrector class
│   ├── tokenization/
│   │   └── tokenizer.py    # Tokenizer class
│   └── utils.py            # Fungsi utility individual
└── demo.py                 # File demo penggunaan
```

## 🆕 Perubahan Versi 1.1.0

- ✅ Menggabungkan spell correction dan slang normalization dalam `SpellCorrector`
- ✅ Semua dataset menggunakan file lokal (CSV/JSON)
- ✅ Struktur yang lebih terorganisir dengan pemisahan kelas dan fungsi
- ✅ Penambahan `DatasetLoader` untuk manajemen dataset terpusat
- ❌ Menghapus dependency HuggingFace untuk dataset
- ❌ Menghapus fitur `preprocess()` all-in-one dan `pipeline()` (akan ditambahkan di versi mendatang)

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
