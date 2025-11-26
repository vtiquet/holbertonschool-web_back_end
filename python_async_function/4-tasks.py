#!/usr/bin/env python3
"""
Altered wait_n function that uses task_wait_random to create Tasks.
"""
import asyncio
from typing import List

# Import task_wait_random from Task 3
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of all the delays in ascending order.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay for each call.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    # Implementation is nearly identical to wait_n, but uses task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
