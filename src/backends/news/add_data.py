from flask import Blueprint, request
import requests
from bs4 import Beautifulsoup
from backends.models import Newssource

class add_data:
    def __init__(self, url="", pattern="", name="", tag=""):
        self.url = url
        self.pattern = pattern
        self.name = name
        self.tag = tag

    def verify(self):
        url = self.url
        response = requests.get(url)
        if 200 <= response.status_code <= 299 and len(response.content) > 0:
            return True
        return False
    
    def check_pattern(self):
        pattern = self.pattern
        url = self.url
        response = requests.get(url)
        soup = Beautifulsoup(response.content, "html.parser")
        result = soup.find_all(pattern)



    def add(self, url, name, tag, pattern):
        self.url = url
        verified = self.verify(self.url):
        if not verified:
            return "Not able to add url because it was a faulty url"
        self.pattern = pattern
        self.tag = tag
        new = Newssource(name=name, url=url)
    