import requests

URL = "http://127.0.0.1:5090/api/shop/item/add"

data = {"title":"test3", "description":"this is a description again 3", "price":"4", "stock":2}

res = requests.post(URL, json=data)
print(res.json())