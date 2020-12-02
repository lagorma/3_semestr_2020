#!/bin/python
import aiohttp
import asyncio
from aiofile import LineReader, AIOFile, Writer
import re


async def help_func(name,name2):
    async with AIOFile(name, 'r') as file:
        async for line in LineReader(file):
            print(f'I\'m here: {line[:-2:]}')
            async with aiohttp.ClientSession() as session:
                async with session.get(line) as response:
                    text_file = await response.text()
                    #print(text_file)
                    text_file = re.split(r'[\r\n]', str(text_file))
                    print(f'Lines that start with <a :')
                    for el in text_file:
                        if el.strip().startswith('<a '):
                            print(el)
                            async with AIOFile(name2, 'a') as file:
                                writer = Writer(file)
                                await writer(f'{el}\n')
    print('I finished')



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    with open('str.txt','w') as f:
        pass
    loop.run_until_complete(help_func("urls.txt",'str.txt'))
