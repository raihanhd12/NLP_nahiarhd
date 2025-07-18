"""
Spell corrector untuk Bahasa Indonesia (menggunakan indonesia_spellchecker).
"""

import difflib
import json
import os

from nahiarhdNLP.preprocessing.cleaning.indonesia_spellchecker import main as indo_spell


class SpellCorrector:
    """Spell correction untuk bahasa Indonesia."""

    def __init__(self):
        # Pastikan path ke wordlist.json benar
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.old_cwd = os.getcwd()
        self.spell_dir = os.path.join(base_dir, "indonesia_spellchecker")

    def correct(self, word: str) -> str:
        os.chdir(self.spell_dir)
        try:
            # Jika kata sudah ada di kamus, return apa adanya
            if word.lower() in indo_spell.NWORDS:
                return word
            result_json = indo_spell.spellCheck(word)
            result = json.loads(result_json)
            if result and isinstance(result, list) and result[0].get("suggestion"):
                suggestion = result[0]["suggestion"]
                if suggestion:
                    ratio = difflib.SequenceMatcher(
                        None, word.lower(), suggestion[0].lower()
                    ).ratio()
                    if ratio >= 0.8:
                        return suggestion[0]
            return word
        finally:
            os.chdir(self.old_cwd)

    def correct_sentence(self, text: str) -> str:
        words = text.split()
        corrected = [self.correct(w) for w in words]
        return " ".join(corrected)
