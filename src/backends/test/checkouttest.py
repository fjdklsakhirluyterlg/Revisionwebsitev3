import requests

URL = "http://127.0.0.1:5090/api/shop/checkout/add"

data = {"user_id":1, "objects":["8", "9"]}

res = requests.post(URL, json=data)
print(res.json())