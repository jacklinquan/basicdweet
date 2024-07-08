"""Basic APIs of the free dweet service.

- Author: Quan Lin
- License: MIT
"""

from .basicdweet import (
    __version__,
    BasicDweetError,
    dweet_for,
    get_latest_dweet_for,
    get_dweets_for,
    async_dweet_for,
    async_get_latest_dweet_for,
    async_get_dweets_for,
)

__all__ = [
    "BasicDweetError",
    "dweet_for",
    "get_latest_dweet_for",
    "get_dweets_for",
    "async_dweet_for",
    "async_get_latest_dweet_for",
    "async_get_dweets_for",
]
