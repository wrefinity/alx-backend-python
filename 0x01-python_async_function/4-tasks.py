#!/usr/bin/env python3
""" Async Basic """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    asy_task = [task_wait_random(max_delay) for _ in range(n)]
    com_task = [await t for t in asyncio.as_completed(asy_task)]
    return com_task
