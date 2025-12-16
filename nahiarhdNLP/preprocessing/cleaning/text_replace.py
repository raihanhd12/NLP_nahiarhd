"""
Text replacement utilities: replace emails, links, and user mentions with tokens.

This module provides simple, well-documented functions used by the pipeline.
"""

import re
from typing import Pattern

_EMAIL_RE: Pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
# simple URL pattern covering http(s) and www
_URL_RE: Pattern = re.compile(
    r"(http[s]?://(?:[A-Za-z0-9$-_@.&+!*'(),]|(?:%[0-9A-Fa-f]{2}))+|www\.[A-Za-z0-9.-]+(?:/[A-Za-z0-9._%+-]*)*)"
)
_MENTION_RE: Pattern = re.compile(r"@([A-Za-z0-9_\.\-]+)")


def replace_email_with_token(text: str, token: str = "<email>") -> str:
    """Replace email addresses in `text` with `token`.

    Example:
        replace_email_with_token("Contact me at john.doe@gmail.com")
        -> "Contact me at <email>"
    """
    if not text:
        return text
    return _EMAIL_RE.sub(token, text)


def replace_link_with_token(text: str, token: str = "<link>") -> str:
    """Replace URLs in `text` with `token`.

    Example:
        replace_link_with_token("visit https://example.com") -> "visit <link>"
    """
    if not text:
        return text
    return _URL_RE.sub(token, text)


def replace_user_with_token(text: str, token: str = "<user>") -> str:
    """Replace user mentions (@username) in `text` with `token`.

    Example:
        replace_user_with_token("Hello @alice") -> "Hello <user>"
    """
    if not text:
        return text
    return _MENTION_RE.sub(token, text)
