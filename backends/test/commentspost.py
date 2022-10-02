import requests

URL = "http://127.0.0.1:5090/api/community/add/comment/post"

data = {"text":"test reply", "post_id":2, "author": "armaan", "parent_id":""}

res = requests.post(URL, json=data)
print(res.json())