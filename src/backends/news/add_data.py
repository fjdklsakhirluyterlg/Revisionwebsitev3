from flask import Blueprint, request
import requests
from bs4 import Beautifulsoup
from backends.models import Newssource
from backends import db

class add_data:
    def __init__(self, url="", pattern="", name="", tag="", type_):
        self.url = url
        self.pattern = pattern
        self.name = name
        self.tag = tag
        self.type = type_

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
        if self.type == "xml":
            soup = BeautifulSoup(response.text, features="xml")
        elif self.type == "url":
            soup = Beautifulsoup(response.content, "html.parser")
        result = soup.find_all(tag, class_=pattern)
        if len(result) == 0:
            pat = self.check_pattern()
            tg = self.check_tag()
            if pat and tag:
                return "Error with framework"
            elif pat and not tag:
                return "invalid tag"
            elif tag and not pat:
                return "invalid pattern"
            elif not tag and not pat:
                return "invalid pattern and tag"
        return "valid tag and pattern"

    def check_pattern(self):
        url = self.url
        pattern = self.pattern
        response = requests.get(url)
        soup = Beautifulsoup(response.content, "html.parser")
        result = soup.find_all(class_=pattern)
        if len(result) == 0:
            return False
        return True
    
    def check_tag(self):
        url = self.url
        tag = self.tag
        response = requests.get(url)
        soup = Beautifulsoup(response.content, "html.parser")
        result = soup.find_all(tag)
        if len(result) == 0:
            return False
        return True

    def add(self, url, name, tag, pattern):
        self.url = url
        verified = self.verify(self.url):
        if not verified:
            return "Not able to add url because it was a faulty url"
        self.pattern = pattern
        self.tag = tag
        check = self.check()
        if check != "valid tag and pattern":
            return check
        new = Newssource(name=name, url=url, pattern=pattern, tag=tag)
        db.session.add(new)
        db.session.commit()
        return "added"


class add_url:
    def __init__(self, url, pattern, tag, name):
        new = add_data(type="url")
        self.new = new
        self.pattern = pattern
        self.tag = tag
        self.name = name
    
    def add(self):
        new = self.new
        tag = self.tag
        pattern = self.tag
        name - self.name
        url = self.url
        res = new.add(url=url, name=name, tag=tag, pattern=pattern)
        return res
