from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db

cost = Blueprint("cost", __name__)

@cost.route("/cost/calculators/energy/bath")
def bath_cost_for_user():
    pass