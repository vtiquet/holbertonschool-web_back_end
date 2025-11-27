#!/usr/bin/env python3
"""
Async Comprehensions
"""
import asyncio
from typing import List

# Import the async_generator from the previous task
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    # Use an async list comprehension to collect the yielded values
    return [i async for i in async_generator()]

if __name__ == '__main__':
    async def main():
        print(await async_comprehension())

    asyncio.run(main())
