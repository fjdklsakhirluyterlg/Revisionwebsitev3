import csv
from .sql import get_users

def write_users():
    users = []
    users = get_users()

    with open('users.csv', 'w', newline='') as file:
        fieldnames = ["name", "timestamp", "points", "email"]
        writer = csv.writer(file)
        writer.writerows(users)