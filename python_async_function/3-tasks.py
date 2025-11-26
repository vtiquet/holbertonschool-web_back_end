#!/usr/bin/env python3
"""
Regular function to create an asyncio.Task.
"""
import asyncio

# Import wait_random from Task 0
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        asyncio.Task: A Task object wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
