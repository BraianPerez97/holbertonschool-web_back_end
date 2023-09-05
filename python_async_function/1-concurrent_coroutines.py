#!/usr/bin/env python3
"""Wait random"""
import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Wait random """
    x = await asyncio.gather(*[wait_random(max_delay) for y in range(n)])
    return sorted(x)
