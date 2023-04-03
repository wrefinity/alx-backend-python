#!/usr/bin/env python3
""" async basic """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """a random delay between 0 & max_delay"""
    asy = random.uniform(0, max_delay)
    await asyncio.sleep(asy)
    return asy
