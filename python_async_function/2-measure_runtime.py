#!/usr/bin/env python3
"""
Function to measure the total execution time of concurrent coroutines.
"""
import time
import asyncio
from typing import Callable

# Import wait_n from Task 1
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): The number of times wait_random is called.
        max_delay (int): The maximum delay passed to wait_random.

    Returns:
        float: The average time taken per execution.
    """
    start_time = time.time()

    # Execute the async function and wait for it
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
