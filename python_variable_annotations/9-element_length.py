#!/usr/bin/env python3
"""Type-annotated function element_length."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element and
    its length.

    Args:
        lst: An iterable of sequences (like strings or lists).

    Returns:
        A list of tuples, each containing the item and its integer length.
    """
    return [(i, len(i)) for i in lst]
