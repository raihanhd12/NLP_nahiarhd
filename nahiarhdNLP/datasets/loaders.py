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
            data = [
                {"slang": row["slang"], "formal": row["formal"]}
                for _, row in df.iterrows()
                if pd.notnull(row["slang"]) and pd.notnull(row["formal"])
            ]
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
            for _, row in df.iterrows():
                item = {
                    "emoji": row.get("emoji", ""),
                    "name_id": row.get("name_id", ""),
                    "alias": row.get("alias", ""),
                    "aliases": (
                        eval(row["aliases"])
                        if pd.notnull(row.get("aliases", ""))
                        else []
                    ),
                }
                data.append(item)
            return data
        except Exception as e:
            print(f"Error loading emoji from CSV: {e}")
            return []

    # Fallback-fallback tidak perlu lagi, cache juga dihapus
