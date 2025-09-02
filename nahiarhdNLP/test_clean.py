from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from nahiarhdNLP.preprocessing import (
    EmojiConverter,
    Pipeline,
    SpellCorrector,
    Stemmer,
    StopwordRemover,
    TextCleaner,
    Tokenizer,
    emoji_to_words,
    pipeline,
    preprocess,
    remove_emoji,
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
    replace_repeated_chars,
    replace_spell_corrector,
    stem_text,
    to_lowercase,
    tokenize,
    words_to_emoji,
)


def demo_functions(console):
    console.print(Panel.fit("[bold blue]Demo Fungsi Utility[/bold blue]", style="blue"))
    tests = [
        ("remove_html", "website <a href='https://google.com'>google</a>", remove_html),
        ("remove_emoji", "Halo dunia 😀😁 apa kabar? 🎉", remove_emoji),
        ("remove_url", "kunjungi https://google.com sekarang!", remove_url),
        ("remove_mentions", "Halo @user123 apa kabar?", remove_mentions),
        ("remove_hashtags", "Hari ini #senin #libur #weekend", remove_hashtags),
        ("remove_numbers", "Saya berumur 25 tahun dan punya 3 anak", remove_numbers),
        (
            "remove_punctuation",
            "Halo, apa kabar?! Semoga sehat selalu...",
            remove_punctuation,
        ),
        ("remove_extra_spaces", "Halo    dunia   yang    indah", remove_extra_spaces),
        ("remove_special_chars", "Halo @#$%^&*() dunia!!!", remove_special_chars),
        ("remove_whitespace", "Halo\n\tdunia\r\nyang indah", remove_whitespace),
        ("to_lowercase", "HALO Dunia Yang INDAH", to_lowercase),
        ("replace_repeated_chars", "kenapaaa???", replace_repeated_chars),
        ("replace_spell_corrector", "emg siapa yg nanya?", replace_spell_corrector),
        ("remove_stopwords", "siapa yang suruh makan?!!", remove_stopwords),
        ("emoji_to_words", "emoji 😀😁", emoji_to_words),
        ("words_to_emoji", "emoji wajah_gembira", words_to_emoji),
        (
            "correct_sentence",
            "sya suka mkn nasi",
            lambda t: SpellCorrector().correct_sentence(t),
        ),
        ("stem_text", "bermain-main dengan senang", stem_text),
        ("tokenize", "Saya suka makan nasi", lambda t: str(tokenize(t))),
    ]
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Fungsi")
    table.add_column("Input")
    table.add_column("Output")
    for name, text, func in tests:
        try:
            output = func(text)
        except Exception as e:
            output = f"[red]Error: {e}[/red]"
        table.add_row(name, text, str(output))
    console.print(table)


def demo_class(console):
    console.print(
        Panel.fit(
            "[bold yellow]Demo Class-based (TextCleaner, StopwordRemover, EmojiConverter, SpellCorrector, Stemmer, Tokenizer)[/bold yellow]",
            style="yellow",
        )
    )
    # TextCleaner
    cleaner = TextCleaner()
    url_text = "kunjungi https://google.com sekarang!"
    mention_text = "Halo @user123 apa kabar?"
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Class")
    table.add_column("Fitur")
    table.add_column("Input")
    table.add_column("Output")
    table.add_row("TextCleaner", "clean_urls", url_text, cleaner.clean_urls(url_text))
    table.add_row(
        "TextCleaner",
        "clean_mentions",
        mention_text,
        cleaner.clean_mentions(mention_text),
    )
    # Test emoji removal
    emoji_text = "Halo dunia 😀😁 apa kabar? 🎉"
    table.add_row(
        "TextCleaner",
        "clean_emoji",
        emoji_text,
        cleaner.clean_emoji(emoji_text),
    )
    # StopwordRemover
    stopword = StopwordRemover()
    stopword._load_data()
    text = "saya suka makan nasi goreng"
    table.add_row(
        "StopwordRemover", "remove_stopwords", text, stopword.remove_stopwords(text)
    )
    # EmojiConverter
    emoji = EmojiConverter()
    emoji._load_data()
    emoji_text = "😀 😂 😍"
    table.add_row(
        "EmojiConverter",
        "emoji_to_text_convert",
        emoji_text,
        emoji.emoji_to_text_convert(emoji_text),
    )
    text3 = "wajah_gembira"
    table.add_row(
        "EmojiConverter",
        "text_to_emoji_convert",
        text3,
        emoji.text_to_emoji_convert(text3),
    )
    # SpellCorrector (now handles both spell correction and slang normalization)
    try:
        spell = SpellCorrector()
        spell_text = "sya suka mkn nasi"
        table.add_row(
            "SpellCorrector",
            "correct_sentence",
            spell_text,
            spell.correct_sentence(spell_text),
        )
        # Test slang normalization capability
        slang_text = "gw lg di rmh"
        table.add_row(
            "SpellCorrector",
            "slang_normalization",
            slang_text,
            spell.correct_sentence(slang_text),
        )
    except Exception as e:
        table.add_row(
            "SpellCorrector", "correct_sentence", "-", f"[red]Error: {e}[/red]"
        )
    # Stemmer
    try:
        stemmer = Stemmer()
        stem_text_in = "bermain-main dengan senang"
        table.add_row("Stemmer", "stem", stem_text_in, stemmer.stem(stem_text_in))
    except Exception as e:
        table.add_row("Stemmer", "stem", "-", f"[red]Error: {e}[/red]")
    # Tokenizer
    tokenizer = Tokenizer()
    token_text = "Saya suka makan nasi"
    table.add_row(
        "Tokenizer", "tokenize", token_text, str(tokenizer.tokenize(token_text))
    )
    console.print(table)


def demo_pipeline(console):
    """Demo fitur Pipeline untuk preprocessing sekaligus."""
    console.print(
        Panel.fit(
            "[bold green]🔀 Demo Pipeline - Preprocessing Sekaligus[/bold green]",
            style="green",
        )
    )

    # Sample messy text untuk testing
    messy_text = "Halooo @user123 #trending https://example.com gw lg nyari info pnting 😀!!! 123"

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metode")
    table.add_column("Konfigurasi/Parameter")
    table.add_column("Input")
    table.add_column("Output")

    # 1. Demo Kelas Pipeline - Default Config
    try:
        pipe_default = Pipeline()
        result1 = pipe_default.process(messy_text)
        table.add_row(
            "Pipeline (default)",
            "Konfigurasi default",
            messy_text[:50] + "...",
            str(result1),
        )
    except Exception as e:
        table.add_row(
            "Pipeline (default)",
            "Konfigurasi default",
            messy_text[:50] + "...",
            f"[red]Error: {e}[/red]",
        )

    # 2. Demo Kelas Pipeline - Custom Config
    try:
        custom_config = {
            "remove_url": True,
            "remove_mentions": True,
            "remove_hashtags": True,
            "remove_numbers": True,
            "replace_spell_corrector": True,
            "correct_sentence": True,
            "to_lowercase": True,
            "remove_punctuation": True,
        }
        pipe_custom = Pipeline(custom_config)
        result2 = pipe_custom.process(messy_text)
        table.add_row(
            "Pipeline (custom)",
            "URL, mentions, hashtags, numbers, slang, spelling, lowercase, punctuation",
            messy_text[:50] + "...",
            str(result2),
        )
    except Exception as e:
        table.add_row(
            "Pipeline (custom)",
            "Custom config",
            messy_text[:50] + "...",
            f"[red]Error: {e}[/red]",
        )

    # 3. Demo Pipeline dengan tokenisasi
    try:
        tokenize_config = {
            "remove_url": True,
            "remove_mentions": True,
            "replace_spell_corrector": True,
            "to_lowercase": True,
            "tokenize": True,
        }
        pipe_token = Pipeline(tokenize_config)
        result3 = pipe_token.process("gw suka makan nasi @user")
        table.add_row(
            "Pipeline (tokenize)",
            "URL, mentions, slang, lowercase + tokenize",
            "gw suka makan nasi @user",
            str(result3),
        )
    except Exception as e:
        table.add_row(
            "Pipeline (tokenize)",
            "With tokenization",
            "gw suka makan nasi @user",
            f"[red]Error: {e}[/red]",
        )

    # 4. Demo fungsi pipeline()
    try:
        simple_config = {
            "remove_url": True,
            "replace_spell_corrector": True,
            "to_lowercase": True,
        }
        result4 = pipeline("Gw lg browsing https://google.com", simple_config)
        table.add_row(
            "pipeline() function",
            "URL, slang, lowercase",
            "Gw lg browsing https://google.com",
            str(result4),
        )
    except Exception as e:
        table.add_row(
            "pipeline() function",
            "Simple config",
            "Gw lg browsing https://google.com",
            f"[red]Error: {e}[/red]",
        )

    # 5. Demo fungsi preprocess()
    try:
        result5 = preprocess(
            "Halooo @user!!! 123",
            remove_mentions=True,
            remove_numbers=True,
            remove_punctuation=True,
            replace_repeated_chars=True,
            to_lowercase=True,
            replace_spell_corrector=False,
        )
        table.add_row(
            "preprocess() function",
            "mentions, numbers, punctuation, elongation, lowercase",
            "Halooo @user!!! 123",
            str(result5),
        )
    except Exception as e:
        table.add_row(
            "preprocess() function",
            "Explicit parameters",
            "Halooo @user!!! 123",
            f"[red]Error: {e}[/red]",
        )

    console.print(table)


def main():
    console = Console()
    console.print(
        Text("🇮🇩 [bold blue]nahiarhdNLP Demo Lengkap[/bold blue]", style="bold blue")
    )
    console.print(Text("Demonstrasi SEMUA Fungsi & Class Library", style="italic"))
    console.print("=" * 80)
    demo_functions(console)
    console.print("\n" + "=" * 80)
    demo_class(console)
    console.print("\n" + "=" * 80)
    demo_pipeline(console)
    console.print("\n" + "=" * 80)
    console.print(
        Panel.fit(
            "[bold green]🎉 Selesai! Semua fitur utama sudah didemokan.\n"
            "Termasuk fitur BARU: Pipeline untuk preprocessing sekaligus![/bold green]",
            style="bold green",
        )
    )


def demo_text_cleaner():
    """Demo function for regular TextCleaner (removes text completely)."""
    console = Console()

    console.print(
        Panel.fit(
            "[bold blue]Demo TextCleaner (Complete Removal)[/bold blue]", style="blue"
        )
    )

    # Create TextCleaner instance with default options
    cleaner = TextCleaner()

    # Sample texts for testing
    test_cases = {
        "urls": "Check this link: http://example.com and https://google.com",
        "mentions": "Hello @user1 and @user2, how are you?",
        "hashtags": "I love #cars and #bikes",
        "numbers": "I have 123 apples and 456 oranges",
        "punctuation": "Hello! How are you? I'm fine, thanks.",
        "lowercase": "HELLO WORLD",
        "extra_spaces": "Hello    world   !",
        "repeated_chars": "Hiiiiii thereeee!!!",
        "special_chars": "Hello @#$% world!",
        "html": "<p>Hello <b>world</b>!</p>",
        "emoji": "Hello 😀 world 🌍",
        "whitespace": "Hello\tworld\n!",
        "emails": "Contact me at john.doe@gmail.com or jane@example.org",
        "phones": "Call me at (555) 123-4567 or +62 812-3456-7890",
        "currency": "The price is $100.50, €75.25, and Rp 500.000",
        "mixed": "Hello @user! Check #cars at http://example.com 😀",
    }

    print("\n=== TextCleaner Test Results ===\n")
    print("Current options:", cleaner.get_options())
    print("\n" + "=" * 50 + "\n")

    # Test each method
    methods = [
        ("clean_urls", "urls"),
        ("clean_mentions", "mentions"),
        ("clean_hashtags", "hashtags"),
        ("clean_numbers", "numbers"),
        ("clean_punctuation", "punctuation"),
        ("to_lowercase", "lowercase"),
        ("clean_extra_spaces", "extra_spaces"),
        ("clean_repeated_chars", "repeated_chars"),
        ("clean_special_chars", "special_chars"),
        ("clean_html", "html"),
        ("clean_emoji", "emoji"),
        ("clean_whitespace", "whitespace"),
    ]

    for method_name, test_key in methods:
        method = getattr(cleaner, method_name)
        input_text = test_cases[test_key]
        output_text = method(input_text)

        console.print(f"[bold yellow]Method:[/bold yellow] {method_name}")
        console.print(f"[green]Input:[/green]  '{input_text}'")
        console.print(f"[blue]Output:[/blue] '{output_text}'")
        console.print("-" * 40)

    # Test mixed case
    console.print("\n[bold cyan]=== Mixed Test Case ===[/bold cyan]")
    mixed_input = test_cases["mixed"]
    console.print(f"[green]Original:[/green] '{mixed_input}'")

    # Apply all cleaning methods in sequence
    result = mixed_input
    for method_name, _ in methods:
        method = getattr(cleaner, method_name)
        result = method(result)
        console.print(f"[yellow]After {method_name}:[/yellow] '{result}'")

    console.print("\n[bold green]=== Final Result ===[/bold green]")
    console.print(f"[bold blue]'{result}'[/bold blue]")


def demo_word_preserving_cleaner():
    """Demo function for Word-Preserving TextCleaner (keeps meaningful content)."""
    console = Console()

    console.print(
        Panel.fit(
            "[bold green]Demo Word-Preserving TextCleaner (BARU!)[/bold green]",
            style="green",
        )
    )

    # Create Word-Preserving TextCleaner instance with new features enabled
    from nahiarhdNLP.preprocessing.cleaning.text_cleaner_word import (
        TextCleaner as WordTextCleaner,
    )

    cleaner = WordTextCleaner(
        remove_urls=True,
        remove_mentions=True,
        remove_hashtags=True,
        clean_emails=True,  # Enable email cleaning
        clean_phones=True,  # Enable phone cleaning
        clean_currency=True,  # Enable currency cleaning
    )

    # Sample texts for testing new features
    test_cases = {
        "urls": "Check this link: http://example.com and https://google.com",
        "mentions": "Hello @user1 and @user2, how are you?",
        "hashtags": "I love #cars and #bikes",
        "emails": "Contact me at john.doe@gmail.com or jane@example.org",
        "phones": "Call me at (555) 123-4567 or +62 812-3456-7890",
        "currency": "The price is $100.50, €75.25, and Rp 500.000",
        "mixed": "Hello @user! Check #cars at https://google.com, contact john@gmail.com, call (555)123-4567, price $100",
    }

    console.print(
        "\n[bold yellow]=== Word-Preserving TextCleaner Test Results ===[/bold yellow]"
    )
    console.print(f"[cyan]Current options:[/cyan] {cleaner.get_options()}")
    console.print("\n" + "=" * 50 + "\n")

    # Test each method
    methods = [
        ("clean_urls", "urls"),
        ("clean_mentions", "mentions"),
        ("clean_hashtags", "hashtags"),
        ("clean_emails", "emails"),
        ("clean_phones", "phones"),
        ("clean_currency", "currency"),
    ]

    for method_name, test_key in methods:
        method = getattr(cleaner, method_name)
        input_text = test_cases[test_key]
        output_text = method(input_text)

        console.print(f"[bold yellow]Method:[/bold yellow] {method_name}")
        console.print(f"[green]Input:[/green]  '{input_text}'")
        console.print(f"[blue]Output:[/blue] '{output_text}'")
        console.print("-" * 40)

    # Test mixed case with all new features
    console.print("\n[bold cyan]=== Mixed Test Case (All New Features) ===[/bold cyan]")
    mixed_input = test_cases["mixed"]
    console.print(f"[green]Original:[/green] '{mixed_input}'")

    # Apply all cleaning methods in sequence
    result = cleaner.clean_all(mixed_input)
    console.print(f"[bold magenta]After clean_all():[/bold magenta] '{result}'")

    console.print("\n[bold green]=== Word-Preserving Result ===[/bold green]")
    console.print(f"[bold blue]'{result}'[/bold blue]")
    console.print(
        "\n[italic green]✅ Notice: URLs, mentions, hashtags are cleaned but meaningful content is preserved![/italic green]"
    )
    console.print(
        "[italic green]✅ Email addresses become readable text, phone numbers keep digits, currency keeps numbers![/italic green]"
    )


if __name__ == "__main__":
    main()

    # Also run TextCleaner demo
    print("\n" + "=" * 80 + "\n")
    demo_text_cleaner()

    # Run Word-Preserving TextCleaner demo
    print("\n" + "=" * 80 + "\n")
    demo_word_preserving_cleaner()
