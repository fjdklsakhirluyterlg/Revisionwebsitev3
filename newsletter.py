from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import Emaillist

newsletter = Blueprint("newsletter", __name__)

@newsletter.route('/newsletter')
def show_emails():
    emails = db.session.query(Emaillist.emailadd).all()
    return render_template("newsletter.html", msg=emails)

@newsletter.route("/newsletter/add", methods=["POST", "GET"])
def add_newsletter():
    try:
        if request.method == "POST":
            emails = db.session.query(Emaillist.emailadd).all()
            emailx = request.form.get("newsletter")
            if emailx in emails:
                flash("Already subscribed!", category="error")
            else:
                new_email = Emaillist(emailadd=str(emailx))
                db.session.add(new_email)
                db.session.commit()
                return redirect(url_for("show_emails"))
        else:
            return "What?"
    except Exception as e:
        return f"Could not be carried out because {e}" 