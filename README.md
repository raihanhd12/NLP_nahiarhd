# nahiarhdNLP - Advanced Indonesian Natural Language Processing Library

Advanced Indonesian Natural Language Processing Library dengan fitur preprocessing teks, normalisasi slang, konversi emoji, koreksi ejaan, dan banyak lagi.

## 🚀 Instalasi

```bash
pip install nahiarhdNLP
```

## 📦 Import Library

```python
# Import package utama
import nahiarhdNLP

# Import module preprocessing
from nahiarhdNLP import preprocessing

# Import module datasets
from nahiarhdNLP import datasets

# Atau import fungsi spesifik
from nahiarhdNLP.preprocessing import preprocess, remove_html, replace_slang
```

## Contoh Penggunaan

### 1. 🎯 Fungsi Preprocess All-in-One

```python
from nahiarhdNLP import preprocessing

# Preprocessing lengkap dengan satu fungsi
teks = "Halooo emg siapa yg nanya? 😀"
hasil = preprocessing.preprocess(teks)
print(hasil)
# Output: "halo wajah_gembira"
```

### 2. 🧹 TextCleaner - Membersihkan Teks

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
```

### 3. ✏️ SpellCorrector - Koreksi Ejaan

```python
from nahiarhdNLP.preprocessing import SpellCorrector

spell = SpellCorrector()

# Koreksi kata
word = "mencri"
corrected = spell.correct(word)
print(corrected)
# Output: "mencuri"

# Koreksi kalimat
sentence = "saya mencri informsi"
corrected = spell.correct_sentence(sentence)
print(corrected)
# Output: "saya mencuri informasi"
```

### 4. 🚫 StopwordRemover - Menghapus Stopwords

```python
from nahiarhdNLP.preprocessing import StopwordRemover

stopword = StopwordRemover()

# Menghapus stopwords
text = "saya suka makan nasi goreng"
result = stopword.remove_stopwords(text)
print(result)
# Output: "suka makan nasi goreng"
```

### 5. 🔄 SlangNormalizer - Normalisasi Slang

```python
from nahiarhdNLP.preprocessing import SlangNormalizer

slang = SlangNormalizer()

# Normalisasi kata slang
text = "gw lg di rmh"
result = slang.normalize(text)
print(result)
# Output: "saya lagi di rumah"
```

### 6. 😀 EmojiConverter - Konversi Emoji

```python
from nahiarhdNLP.preprocessing import EmojiConverter

emoji = EmojiConverter()

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

### 7. 🔪 Tokenizer - Tokenisasi

```python
from nahiarhdNLP.preprocessing import Tokenizer

tokenizer = Tokenizer()

# Tokenisasi teks
text = "ini contoh tokenisasi"
tokens = tokenizer.tokenize(text)
print(tokens)
# Output: ['ini', 'contoh', 'tokenisasi']
```

### 8. 🛠️ Fungsi Individual

```python
from nahiarhdNLP.preprocessing import (
    remove_html, remove_url, remove_mentions,
    replace_slang, emoji_to_words, correct_spelling
)

# Menghapus HTML
html_text = "website <a href='https://google.com'>google</a>"
clean_text = remove_html(html_text)
print(clean_text)
# Output: "website google"

# Menghapus URL
url_text = "kunjungi https://google.com sekarang!"
clean_text = remove_url(url_text)
print(clean_text)
# Output: "kunjungi  sekarang!"

# Menghapus mentions
mention_text = "Halo @user123 apa kabar?"
clean_text = remove_mentions(mention_text)
print(clean_text)
# Output: "Halo  apa kabar?"

# Normalisasi slang
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
```

### 9. 📊 Dataset Loader

```python
from nahiarhdNLP.datasets import DatasetLoader

loader = DatasetLoader()

# Load stopwords (dari file CSV lokal)
stopwords = loader.load_stopwords_dataset()
print(f"Jumlah stopwords: {len(stopwords)}")

# Load slang dictionary (dari file CSV lokal)
slang_dict = loader.load_slang_dataset()
print(f"Jumlah slang: {len(slang_dict)}")

# Load emoji dictionary (dari file CSV lokal)
emoji_dict = loader.load_emoji_dataset()
print(f"Jumlah emoji: {len(emoji_dict)}")
```

> **Catatan:** Semua dataset (stopword, slang, emoji) di-load langsung dari file CSV di folder `nahiarhdNLP/datasets/`. Tidak ada proses cache atau download dari HuggingFace.

### 10. 🔄 Pipeline Custom

```python
from nahiarhdNLP.preprocessing import pipeline, replace_word_elongation, replace_slang

# Buat pipeline custom
custom_pipeline = pipeline([
    replace_word_elongation,
    replace_slang
])

# Jalankan pipeline
text = "Knp emg gk mw makan kenapaaa???"
result = custom_pipeline(text)
print(result)
# Output: "mengapa memang tidak mau makan mengapa???"
```

## ⚙️ Parameter Preprocess

Fungsi `preprocess()` memiliki parameter opsional:

```python
result = nahiarhdNLP.preprocessing.preprocess(
    text="Halooo emg siapa yg nanya? 😀",
    remove_html_tags=True,      # Hapus HTML tags
    remove_urls=True,           # Hapus URL
    remove_stopwords_flag=True, # Hapus stopwords
    replace_slang_flag=True,    # Normalisasi slang
    replace_elongation=True,    # Atasi word elongation
    convert_emoji=True,         # Konversi emoji
    correct_spelling_flag=False,# Koreksi ejaan (lambat)
    stem_text_flag=False,       # Stemming
    to_lowercase=True           # Lowercase
)
```

## 🚨 Error Handling

```python
try:
    from nahiarhdNLP import preprocessing
    result = preprocessing.preprocess("test")
except ImportError:
    print("Package nahiarhdNLP belum terinstall")
    print("Install dengan: pip install nahiarhdNLP")
except Exception as e:
    print(f"Error: {e}")
```

## 💡 Tips Penggunaan

1. **Untuk preprocessing cepat**: Gunakan `preprocess()` dengan parameter default
2. **Untuk kontrol penuh**: Gunakan kelas individual (`TextCleaner`, `SpellCorrector`, dll)
3. **Untuk kustomisasi**: Gunakan `pipeline()` dengan fungsi yang diinginkan
4. **Untuk koreksi ejaan**: Aktifkan `correct_spelling_flag=True` (tapi lebih lambat)
5. **Untuk stemming**: Aktifkan `stem_text_flag=True` (perlu install Sastrawi)
6. **Untuk performa optimal**: Dataset akan di-cache otomatis setelah download pertama
7. **Untuk development**: Gunakan fallback data jika HuggingFace down

## ⚡ Performance & Caching

Mulai versi terbaru, nahiarhdNLP **tidak lagi menggunakan cache atau download dataset dari HuggingFace**. Semua dataset di-load langsung dari file CSV lokal yang sudah disediakan di folder `nahiarhdNLP/datasets/`.

- Tidak ada proses cache otomatis
- Tidak ada fallback data
- Tidak ada dependensi ke HuggingFace untuk dataset

## 📦 Dependencies

Package ini membutuhkan:

- `pandas` - untuk load dan proses dataset CSV
- `sastrawi` - untuk stemming (opsional)
- `rich` - untuk output formatting
