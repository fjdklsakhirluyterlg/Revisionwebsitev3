import requests

URL = "http://127.0.0.1:5090/api/shop/item/add"

data = {"title":"test", "description":"this is a description", "price":"10", "stock":3}

res = requests.post(URL, json=data)
print(res.json())