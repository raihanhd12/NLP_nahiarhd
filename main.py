#!/usr/bin/env python3
"""
Demo penggunaan library nahiarhdNLP
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Import fungsi preprocessing
from nahiarhdNLP.preprocessing import (  # Fungsi-fungsi pembersihan individual
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

console = Console()


def demo_basic_functions():
    """Demo fungsi-fungsi dasar preprocessing."""
    console.print(Panel.fit("🔧 Demo Fungsi Dasar Preprocessing", style="bold blue"))

    # Demo remove_html
    console.print("\n[bold cyan]1. remove_html[/bold cyan]")
    html_text = "website <a href='https://google.com'>google</a>"
    result = remove_html(html_text)
    console.print(f"Input:  {html_text}")
    console.print(f"Output: {result}")

    # Demo remove_url
    console.print("\n[bold cyan]2. remove_url[/bold cyan]")
    url_text = "retrieved from https://gist.github.com/gruber/8891611"
    result = remove_url(url_text)
    console.print(f"Input:  {url_text}")
    console.print(f"Output: {result}")

    # Demo remove_stopwords
    console.print("\n[bold cyan]3. remove_stopwords[/bold cyan]")
    stopword_text = "siapa yang suruh makan?!!"
    result = remove_stopwords(stopword_text)
    console.print(f"Input:  {stopword_text}")
    console.print(f"Output: {result}")

    # Demo replace_slang
    console.print("\n[bold cyan]4. replace_slang[/bold cyan]")
    slang_text = "emg siapa yg nanya?"
    result = replace_slang(slang_text)
    console.print(f"Input:  {slang_text}")
    console.print(f"Output: {result}")

    # Demo replace_word_elongation
    console.print("\n[bold cyan]5. replace_word_elongation[/bold cyan]")
    elongation_text = "kenapaaa???"
    result = replace_word_elongation(elongation_text)
    console.print(f"Input:  {elongation_text}")
    console.print(f"Output: {result}")

    # Demo emoji_to_words
    console.print("\n[bold cyan]6. emoji_to_words[/bold cyan]")
    emoji_text = "emoji 😀😁"
    result = emoji_to_words(emoji_text)
    console.print(f"Input:  {emoji_text}")
    console.print(f"Output: {result}")

    # Demo words_to_emoji
    console.print("\n[bold cyan]7. words_to_emoji[/bold cyan]")
    words_text = "emoji wajah_gembira"
    result = words_to_emoji(words_text)
    console.print(f"Input:  {words_text}")
    console.print(f"Output: {result}")


def demo_pipeline():
    """Demo fungsi pipeline."""
    console.print(Panel.fit("🔄 Demo Pipeline Preprocessing", style="bold green"))

    # Contoh sesuai dengan yang diminta user
    console.print("\n[bold cyan]Pipeline Example:[/bold cyan]")
    pipe = pipeline([replace_word_elongation, replace_slang])

    input_text = "Knp emg gk mw makan kenapaaa???"
    result = pipe(input_text)

    console.print(f"Pipeline: [replace_word_elongation, replace_slang]")
    console.print(f"Input:  {input_text}")
    console.print(f"Output: {result}")

    # Contoh pipeline yang lebih kompleks
    console.print("\n[bold cyan]Complex Pipeline Example:[/bold cyan]")
    complex_pipe = pipeline(
        [
            remove_html,
            remove_url,
            replace_word_elongation,
            emoji_to_words,
            replace_slang,
            remove_stopwords,
        ]
    )

    complex_input = (
        "Halooo emg siapa yg nanya? 😀 website <a href='https://google.com'>google</a>"
    )
    complex_result = complex_pipe(complex_input)

    console.print(f"Input:  {complex_input}")
    console.print(f"Output: {complex_result}")


def demo_preprocess():
    """Demo fungsi preprocess all-in-one."""
    console.print(Panel.fit("⚡ Demo Preprocess All-in-One", style="bold magenta"))

    # Test dengan berbagai jenis teks
    test_texts = [
        "Halooo emg siapa yg nanya? 😀",
        "Website <a href='https://google.com'>google</a> kenapaaa gak bisa dibuka???",
        "Gw ga tau knp lu marahhhh terus 😢",
        "Makasih bgt udh bantuin gw yg lagi bingungggg",
    ]

    for i, text in enumerate(test_texts, 1):
        console.print(f"\n[bold cyan]Test {i}:[/bold cyan]")
        result = preprocess(text)
        console.print(f"Input:  {text}")
        console.print(f"Output: {result}")


def demo_individual_functions():
    """Demo fungsi-fungsi pembersihan individual."""
    console.print(
        Panel.fit("🔧 Demo Fungsi Pembersihan Individual", style="bold yellow")
    )

    # Demo remove_mentions
    console.print("\n[bold cyan]1. remove_mentions[/bold cyan]")
    mentions_text = "Halo @user123 dan @admin, apa kabar?"
    mentions_result = remove_mentions(mentions_text)
    console.print(f"Input:  {mentions_text}")
    console.print(f"Output: {mentions_result}")

    # Demo remove_hashtags
    console.print("\n[bold cyan]2. remove_hashtags[/bold cyan]")
    hashtags_text = "Hari ini #senin #libur #weekend"
    hashtags_result = remove_hashtags(hashtags_text)
    console.print(f"Input:  {hashtags_text}")
    console.print(f"Output: {hashtags_result}")

    # Demo remove_numbers
    console.print("\n[bold cyan]3. remove_numbers[/bold cyan]")
    numbers_text = "Saya berumur 25 tahun dan punya 3 anak"
    numbers_result = remove_numbers(numbers_text)
    console.print(f"Input:  {numbers_text}")
    console.print(f"Output: {numbers_result}")

    # Demo remove_punctuation
    console.print("\n[bold cyan]4. remove_punctuation[/bold cyan]")
    punctuation_text = "Halo, apa kabar?! Semoga sehat selalu..."
    punctuation_result = remove_punctuation(punctuation_text)
    console.print(f"Input:  {punctuation_text}")
    console.print(f"Output: {punctuation_result}")

    # Demo remove_extra_spaces
    console.print("\n[bold cyan]5. remove_extra_spaces[/bold cyan]")
    spaces_text = "Halo    dunia   yang    indah"
    spaces_result = remove_extra_spaces(spaces_text)
    console.print(f"Input:  {spaces_text}")
    console.print(f"Output: {spaces_result}")

    # Demo remove_special_chars
    console.print("\n[bold cyan]6. remove_special_chars[/bold cyan]")
    special_text = "Halo @#$%^&*() dunia!!!"
    special_result = remove_special_chars(special_text)
    console.print(f"Input:  {special_text}")
    console.print(f"Output: {special_result}")

    # Demo remove_whitespace
    console.print("\n[bold cyan]7. remove_whitespace[/bold cyan]")
    whitespace_text = "Halo\n\tdunia\r\nyang indah"
    whitespace_result = remove_whitespace(whitespace_text)
    console.print(f"Input:  {repr(whitespace_text)}")
    console.print(f"Output: {whitespace_result}")

    # Demo to_lowercase
    console.print("\n[bold cyan]8. to_lowercase[/bold cyan]")
    uppercase_text = "HALO Dunia Yang INDAH"
    lowercase_result = to_lowercase(uppercase_text)
    console.print(f"Input:  {uppercase_text}")
    console.print(f"Output: {lowercase_result}")


def demo_advanced():
    """Demo fungsi advanced lainnya."""
    console.print(Panel.fit("🚀 Demo Fungsi Advanced", style="bold red"))

    # Demo tokenize
    console.print("\n[bold cyan]1. tokenize[/bold cyan]")
    text = "Saya suka makan nasi"
    tokens = tokenize(text)
    console.print(f"Input:  {text}")
    console.print(f"Output: {tokens}")

    # Demo clean_text
    console.print("\n[bold cyan]2. clean_text[/bold cyan]")
    dirty_text = "Halooo!!! @user #trending https://example.com 😀"
    clean_result = clean_text(dirty_text)
    console.print(f"Input:  {dirty_text}")
    console.print(f"Output: {clean_result}")

    # Demo stem_text (jika Sastrawi tersedia)
    console.print("\n[bold cyan]3. stem_text[/bold cyan]")
    try:
        stem_input = "bermain-main dengan senang"
        stem_result = stem_text(stem_input)
        console.print(f"Input:  {stem_input}")
        console.print(f"Output: {stem_result}")
    except ImportError:
        console.print(
            "[yellow]Sastrawi tidak terinstall. Install dengan: pip install Sastrawi[/yellow]"
        )


def main():
    """Main demo function."""
    console.print(
        Text(
            "🇮🇩 nahiarhdNLP - Advanced Indonesian Natural Language Processing Library",
            style="bold blue",
        )
    )
    console.print(Text("Demonstrasi Penggunaan Library", style="italic"))
    console.print("=" * 60)

    # Demo berbagai fungsi
    demo_basic_functions()
    console.print("\n" + "=" * 60)

    demo_individual_functions()
    console.print("\n" + "=" * 60)

    demo_pipeline()
    console.print("\n" + "=" * 60)

    demo_preprocess()
    console.print("\n" + "=" * 60)

    demo_advanced()
    console.print("\n" + "=" * 60)

    # Petunjuk penggunaan
    console.print(
        Panel.fit(
            """
[bold green]Cara Penggunaan:[/bold green]

[cyan]1. Import fungsi yang dibutuhkan:[/cyan]
from src.preprocessing import remove_html, remove_url, pipeline

[cyan]2. Gunakan fungsi langsung:[/cyan]
result = remove_html("website <a href='https://google.com'>google</a>")

[cyan]3. Atau gunakan pipeline:[/cyan]
pipe = pipeline([replace_word_elongation, replace_slang])
result = pipe("Knp emg gk mw makan kenapaaa???")

[cyan]4. Atau gunakan preprocess all-in-one:[/cyan]
result = preprocess("Halooo emg siapa yg nanya? 😀")
    """,
            style="bold yellow",
        )
    )


if __name__ == "__main__":
    main()
