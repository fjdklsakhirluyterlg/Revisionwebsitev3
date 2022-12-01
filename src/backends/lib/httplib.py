import http.client
import asyncio

def get(url: str, method):
    url.replace("https://", "")
    domain = url.split("/", 1)
    conn = http.client.HTTPSConnection(domain[0])
    if domain[1]:
        conn.request(method, domain[1])
    else:
        conn.request(method, "/")
    r1 = conn.getresponse()
    return r1



def main_run():
    res = get("www.python.org/", "GET")
    print(res.status)

main_run()
