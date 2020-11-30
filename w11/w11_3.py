#!/bin/python
from typing import Any, Union, Coroutine
import aiohttp
import asyncio
from aiofile import LineReader, async_open, AIOFile
import re


async def help_func(name):
    async with AIOFile(name, 'r') as file:
        async for line in LineReader(file):
            print(f'I\'m here: {line[:-2:]}')
            async with aiohttp.ClientSession() as session:
                async with session.get(line) as response:
                    text_file = await response.text()
                    text_file = re.split(r'[\r\n]', str(text_file))
                    #print(text_file)
                    print(f'Lines that start with <a >:')
                    for el in text_file:
                        if el.startswith('<a >'):
                            print(el)
                            async with AIOFile('str.txt', 'w') as file:
                                writer = Writer(file)
                                await writer(line)
    print('I finished')



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(help_func("urls.txt"))
