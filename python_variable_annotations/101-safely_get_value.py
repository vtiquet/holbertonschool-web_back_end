#!/usr/bin/env python3
"""Type-annotated function safely_get_value."""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary using a key.

    Args:
        dct: The input dictionary (Mapping).
        key: The key to look up.
        default: The default value to return if the key is not found.

    Returns:
        The value associated with the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
