import requests

URL = "http://127.0.0.1:5090/follow/user"

data = {"current_user":2, "followed":1}

res = requests.post(URL, json=data)
print(res.json())