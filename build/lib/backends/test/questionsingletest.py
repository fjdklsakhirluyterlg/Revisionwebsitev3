import requests

URL = "http://127.0.0.1:5090/api/quiz/add/single"

data = {"question":"test question", "awnser":"test awnser", "type":"text", "error":0, "quiz_id":1}

res = requests.post(URL, json=data)
print(res.json())