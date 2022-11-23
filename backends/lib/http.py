import http.client
import asyncio

async def get(url, method):
    url.replace("https://", "")
    domain = url.split("/", 1)
    conn = http.client.HTTPSConnection(domain[0])
    conn.request(method, domain[1])
    r1 = conn.getresponse()
    print(r1.status, r1.reason)