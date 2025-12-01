#!/usr/bin/env python3
"""
Simple helper function to calculate the start
and end index for a given page and page size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for a given page and page size.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    The function should return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
