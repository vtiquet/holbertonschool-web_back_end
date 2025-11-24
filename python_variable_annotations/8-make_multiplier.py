#!/usr/bin/env python3
"""Type-annotated function make_multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier.

    Args:
        multiplier: The float to multiply by.

    Returns:
        A function that takes a float and returns a float (the product).
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
