import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from backends.models import User
import csv

users = []
query = User.query.all()
for q in query:
    data = [q.name, q.timestamp, q.points, q.email]
    users.append(data)

with open('users.csv', 'w', newline='') as file:
    fieldnames = ["name", "timestamp", "points", "email"]
    writer = csv.writer(file)
    writer.writerows(users)