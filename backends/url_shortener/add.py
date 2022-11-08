from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from backends.models import urlshortner

add_url = Blueprint("add_url", __name__)

