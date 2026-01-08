#!/usr/bin/env python3
"""
Test dengan clean_hashtags (yang menyimpan text).
"""

from nahiarhdNLP.preprocessing import Pipeline

test_input = "semuah ini bikin Beta sadar nona seng tarima Beta ap adanya🙁#palusulteng #kampungnelayan"

print("=" * 80)
print("TEST: CLEAN_HASHTAGS (keep hashtag text)")
print("=" * 80)
print(f"Input:  '{test_input}'")

# Gunakan clean_hashtags, bukan remove_hashtags
config = {
    "clean_hashtags": True,  # ← GANTI dari remove_hashtags
    "remove_emoji": True,
    "remove_lowercase": True,
    "remove_extra_spaces": True,
}

pipeline = Pipeline(config)
result = pipeline.process(test_input)

print(f"Output: '{result}'")
print(
    f"\nExpected: 'semuah ini bikin beta sadar nona seng tarima beta ap adanya palusulteng kampungnelayan'"
)
