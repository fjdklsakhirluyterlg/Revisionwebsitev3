from backends import db
from backends.models import User
import csv

users = []
query = User.query.all()
for q in query:
    data = [q.name, q.created_at]
    users.append()