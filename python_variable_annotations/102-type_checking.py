#!/usr/bin/env python3
"""mypy validation for zoom_array."""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on an array by repeating each element.

    Args:
        lst: A tuple of any type elements.
        factor: The integer factor for zooming.

    Returns:
        A list containing the zoomed-in elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)


zoom_2x = zoom_array(array)


# The factor argument must be an int, so we correct it from 3.0 to 3.
zoom_3x = zoom_array(array, 3)
