import pickle
from pathlib import Path

from datasets import load_dataset


class DatasetLoader:
    """Loader for Indonesian NLP datasets from HuggingFace with caching."""

    def __init__(self):
        # Setup cache directory
        self.cache_dir = Path.home() / ".nahiarhdNLP" / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cached_data(self, dataset_name: str):
        """Get cached dataset if exists."""
        cache_file = self.cache_dir / f"{dataset_name}.pkl"
        if cache_file.exists():
            try:
                with open(cache_file, "rb") as f:
                    return pickle.load(f)
            except Exception:
                # If cache corrupted, remove it
                cache_file.unlink()
        return None

    def _save_cached_data(self, dataset_name: str, data):
        """Save dataset to cache."""
        cache_file = self.cache_dir / f"{dataset_name}.pkl"
        try:
            with open(cache_file, "wb") as f:
                pickle.dump(data, f)
        except Exception as e:
            print(f"Warning: Could not cache {dataset_name}: {e}")

    def load_stopwords_dataset(self, language="indonesian"):
        """Load stopwords with caching."""
        cache_key = f"stopwords_{language}"

        # Try cache first
        cached_data = self._get_cached_data(cache_key)
        if cached_data:
            print(f"Using cached stopwords ({len(cached_data)} words)")
            return cached_data

        # Load from HuggingFace
        print("Loading stopwords from HuggingFace...")
        try:
            ds = load_dataset("nahiar/indo-stopwords")
            data = [item["stopword"] for item in list(ds["train"])]

            # Cache the data
            self._save_cached_data(cache_key, data)
            return data

        except Exception as e:
            print(f"Error loading stopwords: {e}")
            return self._get_fallback_stopwords()

    def load_slang_dataset(self, language="indonesian"):
        """Load slang dataset with caching."""
        cache_key = f"slang_{language}"

        # Try cache first
        cached_data = self._get_cached_data(cache_key)
        if cached_data:
            print(f"Using cached slang ({len(cached_data)} entries)")
            return cached_data

        # Load from HuggingFace
        print("Loading slang from HuggingFace...")
        try:
            ds = load_dataset("nahiar/indonesia-slang")
            data = [
                {"slang": item["slang"], "formal": item["formal"]}
                for item in list(ds["train"])
            ]

            # Cache the data
            self._save_cached_data(cache_key, data)
            return data

        except Exception as e:
            print(f"Error loading slang: {e}")
            return self._get_fallback_slang()

    def load_emoji_dataset(self, language="indonesian"):
        """Load emoji dataset with caching."""
        cache_key = f"emoji_{language}"

        # Try cache first
        cached_data = self._get_cached_data(cache_key)
        if cached_data:
            print(f"Using cached emoji ({len(cached_data)} entries)")
            return cached_data

        # Load from HuggingFace
        print("Loading emoji from HuggingFace...")
        try:
            ds = load_dataset("nahiar/indo-emoji-dictionary")
            data = [dict(item) for item in list(ds["train"])]

            # Cache the data
            self._save_cached_data(cache_key, data)
            return data

        except Exception as e:
            print(f"Error loading emoji: {e}")
            return self._get_fallback_emoji()

    def _get_fallback_stopwords(self):
        """Fallback stopwords if HuggingFace fails."""
        return [
            "yang",
            "dan",
            "di",
            "ke",
            "dari",
            "untuk",
            "dengan",
            "ini",
            "itu",
            "atau",
            "juga",
            "bisa",
            "akan",
            "sudah",
            "belum",
            "tidak",
            "bukan",
            "saya",
            "kamu",
            "dia",
            "mereka",
            "kami",
            "kita",
            "anda",
            "beliau",
        ]

    def _get_fallback_slang(self):
        """Fallback slang if HuggingFace fails."""
        return [
            {"slang": "gw", "formal": "saya"},
            {"slang": "gue", "formal": "saya"},
            {"slang": "lo", "formal": "kamu"},
            {"slang": "lu", "formal": "kamu"},
            {"slang": "yg", "formal": "yang"},
            {"slang": "dgn", "formal": "dengan"},
            {"slang": "utk", "formal": "untuk"},
            {"slang": "dr", "formal": "dari"},
            {"slang": "tp", "formal": "tapi"},
            {"slang": "krn", "formal": "karena"},
            {"slang": "jd", "formal": "jadi"},
            {"slang": "sdh", "formal": "sudah"},
            {"slang": "udh", "formal": "sudah"},
            {"slang": "blm", "formal": "belum"},
            {"slang": "ga", "formal": "tidak"},
            {"slang": "gak", "formal": "tidak"},
            {"slang": "nggak", "formal": "tidak"},
            {"slang": "bgt", "formal": "banget"},
            {"slang": "klo", "formal": "kalau"},
            {"slang": "gimana", "formal": "bagaimana"},
            {"slang": "gmn", "formal": "bagaimana"},
            {"slang": "kenapa", "formal": "mengapa"},
            {"slang": "knp", "formal": "mengapa"},
            {"slang": "makasih", "formal": "terima kasih"},
            {"slang": "mksh", "formal": "terima kasih"},
            {"slang": "org", "formal": "orang"},
            {"slang": "skrg", "formal": "sekarang"},
            {"slang": "trs", "formal": "terus"},
            {"slang": "emg", "formal": "memang"},
            {"slang": "kyk", "formal": "seperti"},
        ]

    def _get_fallback_emoji(self):
        """Fallback emoji if HuggingFace fails."""
        return [
            {
                "emoji": "😀",
                "name_id": "wajah_gembira",
                "alias": "wajah_gembira",
                "aliases": ["gembira", "senang", "happy"],
            },
            {
                "emoji": "😂",
                "name_id": "wajah_tertawa",
                "alias": "wajah_tertawa",
                "aliases": ["tertawa", "laugh", "ketawa"],
            },
            {
                "emoji": "😍",
                "name_id": "wajah_bercinta",
                "alias": "wajah_bercinta",
                "aliases": ["bercinta", "love", "cinta"],
            },
            {
                "emoji": "😭",
                "name_id": "wajah_menangis",
                "alias": "wajah_menangis",
                "aliases": ["menangis", "cry", "sedih"],
            },
            {
                "emoji": "😡",
                "name_id": "wajah_marah",
                "alias": "wajah_marah",
                "aliases": ["marah", "angry", "kesal"],
            },
            {
                "emoji": "👍",
                "name_id": "jempol_keatas",
                "alias": "jempol_keatas",
                "aliases": ["jempol", "thumbs_up", "bagus"],
            },
            {
                "emoji": "👎",
                "name_id": "jempol_kebawah",
                "alias": "jempol_kebawah",
                "aliases": ["jempol_bawah", "thumbs_down", "jelek"],
            },
            {
                "emoji": "❤️",
                "name_id": "hati_merah",
                "alias": "hati_merah",
                "aliases": ["hati", "love", "cinta"],
            },
            {
                "emoji": "🔥",
                "name_id": "api",
                "alias": "api",
                "aliases": ["panas", "fire", "keren"],
            },
            {
                "emoji": "💯",
                "name_id": "seratus",
                "alias": "seratus",
                "aliases": ["100", "perfect", "sempurna"],
            },
        ]

    def clear_cache(self):
        """Clear all cached data."""
        import shutil

        if self.cache_dir.exists():
            shutil.rmtree(self.cache_dir)
            print("Cache cleared!")

    def get_cache_info(self):
        """Get cache information."""
        if not self.cache_dir.exists():
            return "No cache directory"

        cache_files = list(self.cache_dir.glob("*.pkl"))
        total_size = sum(f.stat().st_size for f in cache_files)

        return {
            "cache_dir": str(self.cache_dir),
            "files": len(cache_files),
            "total_size_mb": total_size / 1024 / 1024,
            "files_list": [f.name for f in cache_files],
        }
