#!/bin/python
import asyncio
import aiohttp
from concurrent.futures import ALL_COMPLETED


async def server_request(session,url,i):
    async with session.get(url) as r:
        print(f'Requrest №{i} start')
        html = await r.text()
        print(html)
        print(f'Requrest №{i} stop')
        return html


async def func():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.wait({server_request(session,'http://127.0.0.1:8000',i) for i in range(100)}, return_when=ALL_COMPLETED)


if __name__ == "__main__":
    print('start')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(func())
    print('stop')
