import requests
from bs4 import BeautifulSoup

class UrlFetcher:
    def __init__(self, url, tag, pattern):
        self.url = url
        self.pattern = pattern
        self.tag = tag
    
    def get_data(self):
        URL = self.url
        response = requests.get(URL)

        soup = BeautifulSoup(response.content, "html.parser")
