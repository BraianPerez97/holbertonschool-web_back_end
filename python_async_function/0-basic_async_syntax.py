#!/usr/bin/env python3
"""Wait randomly between 0 and max_delay seconds"""

import random
import asyncio


async def wait_random(max_delay=10):
    """Wait for a random delay between 0 and max_delay seconds
    and return it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
