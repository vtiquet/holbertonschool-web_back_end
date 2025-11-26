#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random delay.
"""
import asyncio
import random
from typing import (
    List,
    TypeVar
)


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (included)
    seconds and eventually returns the delay.

    Args:
        max_delay (int): The maximum number of seconds to wait.
                         Defaults to 10.

    Returns:
        float: The actual random delay waited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
