"""Preprocessing package exports.

Expose `Pipeline` for convenience so callers can do:

        from nahiarhdNLP.preprocessing import Pipeline

"""

from .main import Pipeline  # noqa: F401

__all__ = ["Pipeline"]
