import requests
from bs4 import BeautifulSoup

class UrlFetcher:
    def __init__(self, url, tag, pattern):
        self.url = url
        self.pattern = pattern
        self.tag = tag
    
    def get_data(self):
        response = requests.get(self.url)

        soup = BeautifulSoup(response.content, "html.parser")
        result = soup.find_all(self.tag, class_=self.pattern)
        return result

class RssFetcher:
    def __init__(self, url):
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        self.url = url
        self.headers = headers
    
    def get_data(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all("title")
        return data

def get_simple_flying():
    URL = "https://simpleflying.com/"
    tag = "h3"
    pattern = "bc-title"
    url = UrlFetcher(URL, tag, pattern)
    data = url.get_data()
    return data

def get_bbc_news():
    URL = "https://bbc.co.uk"
    tag = "a"
    pattern = "s-o-faux-block-link"
    url = UrlFetcher(URL, tag, pattern)
    data = url.get_data()
    return data

def get_the_verge():
    URL = "https://www.theverge.com/rss/index.xml"