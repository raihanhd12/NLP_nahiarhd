"""
Test script for TextCleaner from text_cleaner_word.py
"""

from nahiarhdNLP.preprocessing.cleaning.text_cleaner_word import TextCleaner


def test_text_cleaner():
    # Create TextCleaner instance with default options
    cleaner = TextCleaner()

    # Sample texts for testing
    test_cases = {
        "urls": "Check this link: http://example.com and https://google.com",
        "mentions": "Hello @user1 and @user2, how are you?",
        "hashtags": "I love #cars and #bikes",
        "html": "<p>Hello <b>world</b>!</p>",
        "mixed": "Hello @user! Check #cars at http://example.com",
    }

    print("=== TextCleaner Word-Preserving Test Results ===\n")
    print("Current options:", cleaner.get_options())
    print("\n" + "=" * 50 + "\n")

    # Test core methods
    print("Method: clean_urls")
    print(f"Input:  '{test_cases['urls']}'")
    print(f"Output: '{cleaner.clean_urls(test_cases['urls'])}'")
    print("-" * 40)

    print("Method: clean_mentions")
    print(f"Input:  '{test_cases['mentions']}'")
    print(f"Output: '{cleaner.clean_mentions(test_cases['mentions'])}'")
    print("-" * 40)

    print("Method: clean_hashtags")
    print(f"Input:  '{test_cases['hashtags']}'")
    print(f"Output: '{cleaner.clean_hashtags(test_cases['hashtags'])}'")
    print("-" * 40)

    print("Method: clean_html")
    print(f"Input:  '{test_cases['html']}'")
    print(f"Output: '{cleaner.clean_html(test_cases['html'])}'")
    print("-" * 40)

    # Test clean_all method
    print("\n=== clean_all() Method Test ===")
    mixed_input = test_cases["mixed"]
    print(f"Original: '{mixed_input}'")
    all_cleaned = cleaner.clean_all(mixed_input)
    print(f"clean_all(): '{all_cleaned}'")
    print("-" * 40)

    # Test mixed case (step by step)
    print("\n=== Mixed Test Case (Step by Step) ===")
    mixed_input = test_cases["mixed"]
    print(f"Original: '{mixed_input}'")

    # Apply cleaning methods in sequence
    result = mixed_input
    result = cleaner.clean_urls(result)
    print(f"After clean_urls: '{result}'")
    result = cleaner.clean_mentions(result)
    print(f"After clean_mentions: '{result}'")
    result = cleaner.clean_hashtags(result)
    print(f"After clean_hashtags: '{result}'")
    result = cleaner.clean_html(result)
    print(f"After clean_html: '{result}'")

    print("\n=== Final Result ===")
    print(f"'{result}'")


if __name__ == "__main__":
    test_text_cleaner()
