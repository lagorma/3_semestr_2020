#!/bin/python
from typing import Any, Union, Coroutine

import aiohttp
import asyncio
from aiofile import LineReader, async_open, AIOFile
import re


async def func(session, service):
    async with session.get(service) as file:
        text_file = file.text()
        text_file = re.split(r'[\r\n]', text_file)
        for i in text_file:
            if i.startswith('<a >'):
                async with AIOFile('str.txt', 'w') as f:
                    writer = Writer(f)
                    await writer(i)


async def help_func(name):
    async with AIOFile(name, 'r') as file:
        print(file)
        async for line in LineReader(file):
            print(line)
            async with aiohttp.ClientSession() as session:
                asyncio.ensure_future(func(session, line))
        print('I finished')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(help_func("urls.txt"))
    loop.close()
