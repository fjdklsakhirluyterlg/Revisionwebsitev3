import http.client
import asyncio

async def get(url, method):
    url.replace("https://", "")
    domain = url.split("/", 1)
    conn = http.client.HTTPSConnection(domain[0])
    conn.request(method, domain[1])
    r1 = conn.getresponse()
    return r1.status, r1.reason

async def main_run():
    status, reason = asyncio.gather(get())
    print(status)

asyncio.run(main_run())
