#!/usr/bin/env python3
"""
measure_runtime module

This module defines a coroutine that measures the total execution time
of running an asynchronous comprehension coroutine four times in parallel.
"""


import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of four parallel async comprehensions.

    This coroutine uses asyncio.gather to run the async_comprehension
    coroutine four times concurrently. It measures the total elapsed
    time for all four to complete.

    The total runtime is approximately 10 seconds because the four tasks
    run concurrently on a single event loop. The underlying 'async_generator'
    is the bottleneck, as it sleeps for 1 second ten times (totaling 10s).
    Since all four tasks await the same shared generator mechanism, they
    complete at the end of the generator's total 10-second duration,
    not the sum of their individual times (which would be ~40s).

    Returns:
        float: The total time taken to execute the four coroutines in seconds.
    """
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time()
    return end - start

if __name__ == '__main__':
    async def main():
        return await(measure_runtime())

    print(
        asyncio.run(main())
    )
