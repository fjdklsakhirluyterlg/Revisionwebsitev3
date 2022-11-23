import http.client
import asyncio

async def get(url, method):
    url.replace("https://", "")
    domain = url.split("/", 1)
    conn = http.client.HTTPSConnection(domain[0])
    conn.request(method, domain[1])