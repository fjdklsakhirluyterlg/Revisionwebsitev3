import requests

URL = "http://127.0.0.1:5090/api/notes/add"

data = {"user_id":1, "text":"test"}

res = requests.post(URL, json=data)
print(res)