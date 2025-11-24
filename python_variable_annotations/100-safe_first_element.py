#!/usr/bin/env python3
"""Type-annotated function safe_first_element."""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence or None if the sequence is empty.

    Args:
        lst: A sequence of any type (e.g., list, tuple).

    Returns:
        The first element of the sequence or None.
    """
    if lst:
        return lst[0]
    else:
        return None
