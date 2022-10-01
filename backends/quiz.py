from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import Quiz, Category, Question, Qawnser
# from . import app

quiz = Blueprint("quiz", __name__)

@quiz.route("/api/quiz/add", methods=["POST"])
def add_quiz_from_thing():
    data = request.get_json()
    user_id = data["user_id"]
    description = data["description"]
    name = data["name"]
    category = data["category"]
    questionsx = data["questions"]
    questions = [i["question"] for i in questionsx]
    awnsers = [i["awnsers"] for i in questionsx]
    hints = [i["hint"] for i in questionsx]
    new = Quiz(user_id=user_id, description=description, name=name)
    db.session.add(new)
    for c in category:
        present = Category.query.filter_by(name=c).first()
        if present:
            present.quiz.quizend(new)
        else:
            new_category = Category(name=c)
            new_category.quiz.quizend(new)
            db.session.add(new_category)
    for q, a, h in zip(questions, awnsers, hints):
        new_question = Question(question=q, hint=h)
        db.session.add(new_question)
        id = getattr(new_question, 'id')
        for awns in a:
            awnser = awns[0]
            error = awns[1]
            correct = awns[2]
            newawns = Qawnser(awnser=awnser, error=error, question_id = id, correct=correct)
            db.session.add(newawns)
    db.session.commit()
    return jsonify(msg="it worked ?")

@quiz.route("/api/quiz/delete/<id>")
def delete_quiz_from_thing(id):
    quiz = Quiz.query.filter_by(id=id).first()
    db.session.delete(quiz)
    db.session.commit()
    return jsonify("deleted")

@quiz.route("/api/quiz")
def api_view_quizzes():
    quizz = Quiz.query.order_by(Quiz.id)
    dict = {}
    for quiz in quizz:
        name = quiz.name
        description = quiz.description
        categories = quiz.category
        category = [i.name for i in categories]
        dict[name] = {"descirption": description, "categories": category}
    return jsonify(dict)

@quiz.route("/api/question")
def api_view_form():
    id = request.args.get("id")
    q = Question.query.filter_by(id=id).first()
    dict = {}
    awnsers = q.awnser
    for a in awnsers:
        t = a.awnser
        correct = a.correct
        error = a.error
        dict[a.id] = [t, correct, error]
    return {"question": q.question, "awnsers": dict, "hint": q.hint, "quiz": q.quiz_id}

@quiz.route("/api/question/delete")
def api_delete_question():
    id = request.args.get("id")
    question = Question.query.filter_by(id=id).first()
    db.session.delete(question)
    db.session.commit()

@quiz.route("/api/question/awnser/delete")
def api_question_awnser_delete():
    id = request.args.get("id")
    awnser = Qawnser.query.filter_by(id=id).first()
    db.session.delete(awnser)
    db.session.commit()
    
@quiz.route("/api/quiz/delete")
def api_delete_quiz():
    id = request.args.get("id")
    quiz = Quiz.query.filter_by(id=id).first()
    db.session.delete(quiz)
    db.session.commit()

@quiz.route("/api/question/check", methods=["POST"])
def check_if_right_awnser():
    data = request.get_json()
    qid = data["question"]
    awnser = data["answer"]
    question = Question.query.filter_by(id=qid).first()
    correct = False
    for q in question.awnser:
        if type(awnser) is not int or type(awnser) is not float:
            if q.awnser == awnser:
                if q.correct:
                    correct = True
        else:
            try:
                if awnser *  1 - (q.error / 100) <= q.awnser <= awnser * 1 + (q.error / 100):
                    if q.correct:
                        correct = True
            except:
               if q.awnser == awnser:
                if q.correct:
                    correct = True 
    
    act_correct = [l.awnser for l in question.awnser if l.correct]
    
    if correct:
        return jsonify(msg="Correct")
    else:
        return jsonify(msg="Not Correct", correct=act_correct, awnser=awnser)

@quiz.route("/api/quiz/add/single")
def add_single_question_to_quiz():
    data = request.get_json()
    
# app.register_blueprint(quiz, url_prefix="/")