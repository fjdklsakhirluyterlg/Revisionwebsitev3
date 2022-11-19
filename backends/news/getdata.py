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
        out = []
        for i in result:
            out.append(i.get_text())
        return out

class RssFetcher:
    def __init__(self, url, pattern):
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        self.url = url
        self.headers = headers
        self.pattern = pattern
    
    def get_data(self):
        list = []
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, features="xml")
        for p in self.pattern:
            data = soup.find_all(p)
            list.append(data)
        return list
    
    def return_data(self):
        data = self.get_data()
        out = zip(*data)
        return list(out)

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
    pattern = ["title", "id"]
    rss = RssFetcher(URL, pattern)
    return rss.return_data()

def get_cnn():
    URL = "https://cnn.com/"
    tag = "h3"
    pattern = "cd__headline"
    url = UrlFetcher(URL, tag, pattern)
    data = url.get_data()
    return data

def get_the_guardian():
    URL = "https://theguardian.com"
    tag = "a"
    pattern = "u-faux-block-link__overlay js-headline-text"
    url = UrlFetcher(URL, tag, pattern)
    data = url.get_data()
    return data

print(get_the_guardian())