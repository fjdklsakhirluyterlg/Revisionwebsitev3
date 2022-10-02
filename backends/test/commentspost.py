import requests

URL = "http://127.0.0.1:5090/community/add/comment/post"

data = {"text":"test comment", "post_id":1, "author": "armaan", "parent_id":""}

res = requests.post(URL, json=data)
print(res.json())