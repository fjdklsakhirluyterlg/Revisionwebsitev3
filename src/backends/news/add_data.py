from flask import Blueprint, request
import requests


class add_data:
    def __init__(self, url):
        self.url = url

    def verify(self):
        url = self.url
        response = requests.get(url)
        if 200 <= response.status_code <= 299 and len(response.data) > 0:
            return True
        return False

    