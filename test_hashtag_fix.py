#!/usr/bin/env python3
"""
Test script untuk memverifikasi hashtag removal fix dengan spacing yang benar.
"""

from nahiarhdNLP.preprocessing import Pipeline

# Test case dari issue Anda
test_cases = [
    {
        "input": "semuah ini bikin Beta sadar nona seng tarima Beta ap adanya🙁#palusulteng #kampungnelayan",
        "expected": "semuah ini bikin beta sadar nona seng tarima beta ap adanya palusulteng kampungnelayan",
        "description": "Original issue - spacing after hashtag removal",
    },
    {
        "input": "Learning #Python #NLP #MachineLearning today",
        "expected": "learning nlp machinelearning today",
        "description": "Multiple hashtags with spaces",
    },
    {
        "input": "#hashtag1#hashtag2 word",
        "expected": "hashtag1 hashtag2 word",
        "description": "Consecutive hashtags without space",
    },
    {
        "input": "text#hashtag more text",
        "expected": "text hashtag more text",
        "description": "Hashtag without space before",
    },
]

print("=" * 80)
print("TESTING HASHTAG REMOVAL FIX")
print("=" * 80)

for i, test_case in enumerate(test_cases, 1):
    print(f"\n[Test {i}] {test_case['description']}")
    print(f"Input:    '{test_case['input']}'")

    # Create pipeline dengan remove_hashtags = True
    config = {
        "remove_hashtags": True,
        "remove_emoji": True,
        "remove_extra_spaces": True,
        "remove_lowercase": True,
    }
    pipeline = Pipeline(config)
    result = pipeline.process(test_case["input"])

    print(f"Output:   '{result}'")
    print(f"Expected: '{test_case['expected']}'")

    # Check if result matches expected
    if result == test_case["expected"]:
        print("✅ PASS")
    else:
        print("❌ FAIL")
        print(f"   Difference detected!")

print("\n" + "=" * 80)
