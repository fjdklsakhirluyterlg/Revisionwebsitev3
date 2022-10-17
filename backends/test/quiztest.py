import requests

URL = "http://127.0.0.1:5090/api/quiz/add"

data = {"user_id":1, "description":"test again", "name":"test again", "category":["test"]}

res = requests.post(URL, json=data)
print(res.json())