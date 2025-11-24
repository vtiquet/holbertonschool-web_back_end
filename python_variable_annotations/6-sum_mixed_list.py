#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing integers and floats.

    Args:
        mxd_lst: A list of numbers (ints or floats).

    Returns:
        The sum of the elements as a float.
    """
    return sum(mxd_lst)
