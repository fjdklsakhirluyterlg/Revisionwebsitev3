from flask import Blueprint, request
from backends.models import Event, Calendar


calendar_add = Bleuprint("calendar_add", __name__)