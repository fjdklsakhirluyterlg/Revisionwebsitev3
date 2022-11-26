from backends.models import User
from backends import db
import csv

def write_users():
    users = []
    query = User.query.all()
    for q in query:
        data = [q.name, q.timestamp, q.points, q.email]
        users.append(data)

    with open('users.csv', 'w', newline='') as file:
        fieldnames = ["name", "timestamp", "points", "email"]
        writer = csv.writer(file)
        writer.writerows(users)

write_users()