from backends import db
from backends.models import User
import csv

users = []
query = User.query.all()