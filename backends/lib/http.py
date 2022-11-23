import http.client
import asyncio

async def get(url):
    conn = http.client.HTTPSConnection(url)