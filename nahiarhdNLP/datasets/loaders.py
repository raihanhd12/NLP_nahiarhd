import json
from pathlib import Path

import pandas as pd


class DatasetLoader:
    """Loader untuk dataset NLP Indonesia dari file CSV lokal."""

    def __init__(self):
        # Path ke folder datasets
        self.datasets_dir = Path(__file__).parent

    def load_stopwords_dataset(self, language="indonesian"):
        """Load stopwords dari CSV."""
        csv_path = self.datasets_dir / "stop_word.csv"
        try:
            df = pd.read_csv(csv_path)
            # Kolom: stopword
            data = df["stopword"].dropna().astype(str).tolist()
            return data
        except Exception as e:
            print(f"Error loading stopwords from CSV: {e}")
            return []

    def load_slang_dataset(self, language="indonesian"):
        """Load slang dari CSV."""
        csv_path = self.datasets_dir / "slang.csv"
        try:
            df = pd.read_csv(csv_path)
            # Kolom: slang, formal
            data = []
            for idx in range(len(df)):
                slang_val = df.iloc[idx, 0]
                formal_val = df.iloc[idx, 1]
                if pd.notnull(slang_val) and pd.notnull(formal_val):
                    data.append({"slang": str(slang_val), "formal": str(formal_val)})
            return data
        except Exception as e:
            print(f"Error loading slang from CSV: {e}")
            return []

    def load_emoji_dataset(self, language="indonesian"):
        """Load emoji dari CSV."""
        csv_path = self.datasets_dir / "emoji.csv"
        try:
            df = pd.read_csv(csv_path)
            # Kolom: emoji, name_id, alias, aliases (aliases berupa string list)
            data = []
            for idx in range(len(df)):
                row = df.iloc[idx]
                aliases_val = row.get("aliases", "")
                aliases_list = []
                if pd.notnull(aliases_val):
                    aliases_str = str(aliases_val).strip()
                    if aliases_str and aliases_str != "nan":
                        try:
                            aliases_list = eval(aliases_str)
                        except Exception as e:
                            print(f"Error loading emoji from CSV: {e}")
                            aliases_list = []

                item = {
                    "emoji": str(row.get("emoji", "")),
                    "name_id": str(row.get("name_id", "")),
                    "alias": str(row.get("alias", "")),
                    "aliases": aliases_list,
                }
                data.append(item)
            return data
        except Exception as e:
            print(f"Error loading emoji from CSV: {e}")
            return []

    def load_wordlist_dataset(self, language="indonesian"):
        """Load wordlist dari JSON."""
        json_path = self.datasets_dir / "wordlist.json"
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, list) else []
        except Exception as e:
            print(f"Error loading wordlist from JSON: {e}")
            return []
