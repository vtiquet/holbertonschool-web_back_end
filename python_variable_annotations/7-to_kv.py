#!/usr/bin/env python3
"""Type-annotated function to_kv."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and a number and returns a tuple.

    Args:
        k: The string key.
        v: An integer or float value.

    Returns:
        A tuple where the first element is k and the second is the
        square of v (annotated as a float).
    """
    return (k, v ** 2)
