from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import Emaillist
from .functions import send_email_newsletter
from . import app

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

@newsletter.route("/api/newsletter/add")
def api_add_newsletter():
    email = request.args.get("email")
    new_email = Emaillist(emailadd = email)
    db.session.add(new_email)
    db.session.commit()
    return jsonify(message = "worked")

@newsletter.route("/api/newsletter/delete")
def api_delete_newsletter():
    id = request.args.get("id")
    email = db.session.query(Emaillist).filter(Emaillist.id == id).first()
    db.session.delete(email)
    db.session.commit()

@newsletter.route("/api/newsletter/deleteemail")
def api_delete_email_by_email():
    email = request.args.get("email")
    stuff = db.session.query(Emaillist).filter(Emaillist.emailadd == email).first()
    db.session.delete(stuff)
    db.session.commit()

@newsletter.route("/api/newsletter/view")
def api_newsletter_view():
    x = db.session.query(Emaillist.emailadd).all()
    dict = {}
    for i, val in enumerate(x):
        dict[str(i)] = str(val)
    # print(x)
    return dict #jsonify(message="hi")

@newsletter.route("/api/newsletter/update")
def update_newsletter_api(request):
    id = request.args.get("id")
    new_email = request.args.get("email")
    email = db.session.query(Emaillist).filter(Emaillist.id == id).first()
    email.emaillist = new_email
    db.session.commit()
    return jsonify(msg="worked")

@newsletter.route("/api/newsletter/create")
def create_newsletter():
    data = request.get_json()
    content = data["content"]
    emails = db.session.qury(Emaillist.emailadd).all()
    for email in emails:
        send_email_newsletter(email, content)
        
app.register_blueprint(newsletter, url_prefix="/")