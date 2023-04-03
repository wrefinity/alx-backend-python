#!/usr/bin/env python3
""" The basics of async """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    asy_task = [asyncio.create_task(wait_random(max_delay)) for x in range(n)]
    com_task  [await t for t in asyncio.as_completed(asy_task)]
    return com_task
