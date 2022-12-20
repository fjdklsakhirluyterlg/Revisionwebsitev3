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
    
    def check(self):
        pattern = self.pattern
        url = self.url
        tag = self.tag
        response = requests.get(url)
        soup = Beautifulsoup(response.content, "html.parser")
        result = soup.find_all(tag, class_=pattern)
        if len(result) == 0:
            pat = self.check_pattern()
        return "valid tag and pattern"

    def check_pattern(self):
        url = self.url
        pattern = self.pattern
        response = requests.get(url)
        soup = Beautifulsoup(response.content, "html.parser")
        

    def add(self, url, name, tag, pattern):
        self.url = url
        verified = self.verify(self.url):
        if not verified:
            return "Not able to add url because it was a faulty url"
        self.pattern = pattern
        self.tag = tag
        new = Newssource(name=name, url=url)
    