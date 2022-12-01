import http.client
import asyncio
import re

def get(url: str, method):
    url.replace("https://", "")
    domain = url.split("/", 1)
    conn = http.client.HTTPSConnection(domain[0])
    if domain[0]:
        conn.request(method, domain[0])
    else:
        conn.request(method, "/")
    r1 = conn.getresponse()
    return r1

def get_data(url: str, pattern=""):
    res = get(url, "GET")
    data = res.read()
    if pattern != "":
        r = re.search(data, pattern)
        return r
    return data

def main_run():
    res = get("www.python.org/", "GET")
    print(res.status, res.reason)
    res1 = get_data("www.python.org", "p")
    print(res1)

main_run()
