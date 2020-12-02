#!/bin/python
from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(session,service):
    #print(f'I\'m here: {service}')
    async with session.get(service.url) as response:
        html = await response.json()
        return html


async def asynchronous():
    async with aiohttp.ClientSession() as session:
        my_ID = await asyncio.wait({fetch_ip(session, el) for el in SERVICES}, return_when=asyncio.FIRST_COMPLETED)
        #print(my_ID)
        for i in my_ID[0]:
                a = i.result()
                for serv in SERVICES:
                    try:
                        print(a[serv.ip_attr])
                    except:
                        pass

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
