#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
from time import time

# Import the async_comprehension from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing
    async_comprehension four times in parallel.

    The total runtime is roughly 10 seconds because all four calls to
    'async_comprehension' run concurrently using 'asyncio.gather'.
    The underlying 'async_generator' yields 10 times with a 1-second delay,
    making the total execution time of the longest I/O operation 10 seconds.
    The concurrent tasks share this 10-second waiting time.

    Returns:
        float: The total time taken to execute all four instances, in seconds.
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time()
    return end_time - start_time

if __name__ == '__main__':
    async def main():
        return await(measure_runtime())

    print(
        asyncio.run(main())
    )
