import requests
from bs4 import BeautifulSoup

class UrlFetcher:
    def __init__(self, url, pattern):
        self.url = url
        self.pattern = pattern
    
    def get_data(self):
        URL = self.url
        data = requests.get(URL)
        