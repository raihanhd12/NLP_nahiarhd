"""
Test script for TextCleaner from text_cleaner_word.py
"""

from nahiarhdNLP.preprocessing.cleaning.text_cleaner_word import TextCleanerWord


def test_text_cleaner():
    # Create TextCleaner instance with default options
    cleaner = TextCleanerWord()

    # Create TextCleaner instance with email, phone, currency cleaning enabled
    cleaner_extended = TextCleanerWord(
        enable_email_cleaning=True,
        enable_phone_cleaning=True,
        enable_currency_cleaning=True,
    )

    # Sample texts for testing
    test_cases = {
        "urls": "Check this link: http://example.com and https://google.com",
        "mentions": "Hello @user1 and @user2, how are you?",
        "hashtags": "I love #cars and #bikes",
        "html": "<p>Hello <b>world</b>!</p>",
        "emails": "Contact me at john.doe@gmail.com or support@company.com",
        "phones": "Call me at 08123456789 or (021) 123-4567",
        "currency": "The price is $100.50 and €75.25 or Rp 50.000",
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

    # Test extended methods (email, phone, currency)
    print("\n=== Extended Cleaning Methods ===")
    print("Current extended options:", cleaner_extended.get_options())
    print("-" * 40)

    print("Method: clean_emails")
    print(f"Input:  '{test_cases['emails']}'")
    print(f"Output: '{cleaner_extended.clean_emails(test_cases['emails'])}'")
    print("-" * 40)

    print("Method: clean_phones")
    print(f"Input:  '{test_cases['phones']}'")
    print(f"Output: '{cleaner_extended.clean_phones(test_cases['phones'])}'")
    print("-" * 40)

    print("Method: clean_currency")
    print(f"Input:  '{test_cases['currency']}'")
    print(f"Output: '{cleaner_extended.clean_currency(test_cases['currency'])}'")
    print("-" * 40)


if __name__ == "__main__":
    test_text_cleaner()
