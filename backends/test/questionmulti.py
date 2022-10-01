import requests

URL = "http://127.0.0.1:5090/api/quiz/add/multiple"

data = {"question":"question", "quiz_id":1, "awnsers":[{"awnser":"test awnser 1", "correct":False}, {"awnser":"test awnser 2", "correct":False}, {"awnser":"never gonna give you up", "correct":True}]}

res = requests.post(URL, json=data)
print(res.json())