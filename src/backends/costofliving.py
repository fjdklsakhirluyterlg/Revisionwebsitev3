from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort, escape
from . import db

cost = Blueprint("cost", __name__)

@cost.route("/cost/calculators/energy/bath")
def bath_cost_for_user():
    if request.method == "POST":
        volume = request.form["volume"]
        escape(volume)
        start = request.form["start"]
        end = request.form["end"]
        energy = volume * 4.18 * (start - end)
        energyk = energy / 1000
        cost = 0.50 * energyk
        return cost, energy