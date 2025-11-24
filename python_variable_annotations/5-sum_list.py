#!/usr/bin/env python3
"""Type-annotated function sum_list."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Args:
        input_list: A list of floating-point numbers.

    Returns:
        The sum of the elements as a float.
    """
    return sum(input_list)
