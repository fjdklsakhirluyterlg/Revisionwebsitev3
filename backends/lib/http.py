import http.client
import asyncio

async def get(url, method):
    url.replace("https://", "")
    conn = http.client.HTTPSConnection(url)
