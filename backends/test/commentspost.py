import requests

URL = "http://127.0.0.1:5090/api/community/add/comment/post"

data = {"text":"test reply nested", "post_id":3, "author": "armaan", "parent_id":12}

res = requests.post(URL, json=data)
print(res.json())