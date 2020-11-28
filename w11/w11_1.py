#!/bin/python
import asyncio
import uvicorn
from fastapi import FastAPI
from main import main

async def server_request(i):
    print(f'Requrest №{i} start')
    await main()
    print(f'Requrest №{i} stop')


async def func():
    await asyncio.gather(*[server_request(i) for i in range(100)])


if __name__ == "__main__":
    print('start')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(func())
    loop.close()
    print('stop')
