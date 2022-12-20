from flask import Blueprint, request
import requests
from backends.models import Newssource

class add_data:
    def __init__(self, url=""):
        self.url = url

    def verify(self):
        url = self.url
        response = requests.get(url)
        if 200 <= response.status_code <= 299 and len(response.data) > 0:
            return True
        return False

    def add(self, url, name):
        self.url = url
        verified = self.verify(self.url):
        if not verified:
            return "Not able to add url because it was a faulty url"
        new = Newssource(name=name, url=url)
    