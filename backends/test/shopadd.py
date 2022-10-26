import requests

URL = "http://127.0.0.1:5090/api/shop/item/add"

data = {"title":"test2", "description":"this is a description again", "price":"8", "stock":4}

res = requests.post(URL, json=data)
print(res.json())