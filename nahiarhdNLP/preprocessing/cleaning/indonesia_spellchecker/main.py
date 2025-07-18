import collections
import difflib
import json
import os
import re

from .stemmer import Stemmer

wordlist_path = os.path.join(os.path.dirname(__file__), "wordlist.json")
NWORDS = json.loads(open(wordlist_path, "r").read())
stem = Stemmer()


def words(text):
    return re.findall("[a-z]+", text.lower())


def spellCheck(text):
    listword = words(text)
    unmatched_items = [d for d in listword if d not in NWORDS]
    true_unmatched = []
    baseword = None
    if len(unmatched_items) > 0:
        for a in unmatched_items:
            try:
                stemmed = stem.stem_word(a)
                for root, value in stemmed.items():
                    baseword = root
            except:
                baseword = None
            if not baseword:
                # get suggestion
                best_match = difflib.get_close_matches(a, NWORDS)
                true_unmatched.append({"word": a, "suggestion": best_match})

    return json.dumps(true_unmatched, indent=4)


if __name__ == "__main__":
    textToBeCheck = open("teks.txt", "r").read()

    result = spellCheck(textToBeCheck)

    print(result)
