#!/usr/bin/env python3

""" Async Comprehensions """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ parallel aysnc comprehensions """
    start_time = time()
    tasks = [async_comprehension() for _ in range(4)]
    await gather(*tasks)
    end_time = time()
    return (end_time - start_time)
