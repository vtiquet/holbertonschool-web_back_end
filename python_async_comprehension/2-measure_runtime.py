#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
import time

# Import the async_comprehension from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    and measures the total runtime.
    """
    start_time = time.time()

    # Create four tasks for async_comprehension
    tasks = [async_comprehension() for _ in range(4)]

    # Run the tasks concurrently
    await asyncio.gather(*tasks)

    end_time = time.time()
    return end_time - start_time

if __name__ == '__main__':
    async def main():
        return await(measure_runtime())

    print(
        asyncio.run(main())
    )
