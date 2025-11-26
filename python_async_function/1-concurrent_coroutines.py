#!/usr/bin/env python3
"""
Coroutines for running multiple asynchronous functions concurrently.
"""
import asyncio
from typing import List

# Import wait_random from Task 0
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns the list of all the delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    # Implementation will involve asyncio.gather and inserting results
    # into a list in sorted order without using .sort()
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
