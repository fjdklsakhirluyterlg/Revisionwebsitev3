import csv
from .sql import get_users

def write_users():
    users = []
    users = get_users()

    with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        fieldnames = ["name", "timestamp", "points", "email"]
        writer.writerow(fieldnames)
        writer.writerows(users)

write_users()