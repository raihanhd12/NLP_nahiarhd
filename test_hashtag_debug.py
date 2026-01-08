#!/usr/bin/env python3
"""
Test sederhana untuk isolasi masalah.
"""

from nahiarhdNLP.preprocessing.cleaning.text_cleaner import TextCleaner

cleaner = TextCleaner(
    remove_hashtags=True,
    remove_emoji=True,
    remove_extra_spaces=True,
    remove_lowercase=True,
)

# Test case 1: Hanya remove_hashtags
text1 = "semuah ini bikin Beta sadar nona seng tarima Beta ap adanya🙁#palusulteng #kampungnelayan"

print("=" * 80)
print("TEST 1: Remove Hashtags Only")
print("=" * 80)
print(f"Input:  '{text1}'")

result = cleaner.remove_hashtags(text1, force=True)
print(f"After remove_hashtags: '{result}'")

result = cleaner.remove_emoji(result, force=True)
print(f"After remove_emoji: '{result}'")

result = cleaner.remove_lowercase(result, force=True)
print(f"After remove_lowercase: '{result}'")

result = cleaner.remove_extra_spaces(result, force=True)
print(f"After remove_extra_spaces: '{result}'")

print("\n" + "=" * 80)
print("TEST 2: Multiple Hashtags")
print("=" * 80)

text2 = "Learning #Python #NLP #MachineLearning today"
print(f"Input:  '{text2}'")

result = cleaner.remove_hashtags(text2, force=True)
print(f"After remove_hashtags: '{result}'")

result = cleaner.remove_lowercase(result, force=True)
print(f"After remove_lowercase: '{result}'")

result = cleaner.remove_extra_spaces(result, force=True)
print(f"After remove_extra_spaces: '{result}'")
