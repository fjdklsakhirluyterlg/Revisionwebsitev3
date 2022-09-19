from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
import requests
from .models import Snake_leaderboard
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from . import db
from .functions import is_integer_num, coefficient, fib, send_email, get_ecenomic_stuff, get_day_of_the_year, get_user_ip_address, collatz, generateπfrom_random, get_loc_from_ip
import os
from itertools import permutations
import shutil
from .classes import Position
from .api import Randomz
import random, math
import subprocess

home = Blueprint('home', __name__)

@home.route('/')
def hello_world():
    return render_template("index.html")

@home.route('/bitcoin')
def get_bitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()

    x = data["bpi"]["GBP"]["rate"]
    return f"<p>The bitcoin price is {x}, probably dont buy it unless youre in el salvador</p>"

@home.route('/tfl')
def get_tfl():
    def is_tube_on():
        liste = ["District", "Central", "Circle", "Piccadilly", "Bakerloo", "Hammersmith-City", "Jubilee", "Metropolitan", "Victoria", "Northern"]
        bad = []
        status_bad = []
        r = []

        for line in liste:
            reply = requests.get("https://api.tfl.gov.uk/Line/" + line + "/Status")

            data = reply.json()

            Status = (data[0]["lineStatuses"][0]["statusSeverityDescription"])

            if Status != "Good Service":
                bad.homeend(line)
                status_bad.homeend(Status)
        
        for l in bad:
            response = requests.get(f"https://api.tfl.gov.uk/Line/{l}/Status")

            d = response.json()

            reason = (d[0]["lineStatuses"][0]["reason"])
            r.homeend(reason)
        
        return r
    
    return f'<p>The following are problematic: {is_tube_on()}</p>'

@home.route('/physics')
def physics():
    return '<h1> Physics</h1> <p style="text-align:center"> Welcome to the physics homepage, here you can learn about physics</p>'

@home.route('/longitudinal-waves-and-transverse-waves')
def explain_waves():
    x = "<p> A longitudinal wave is when the osicalltions are parralel to the wave motion</p><p>A transverse wave is when the osciallations are perpendicular to the wave motion<p>"
    di = "<div style='background-color: #5c32a8'><p> A longitudinal wave is faster than a transverse wave, this is because there is less firction</p><p> A longitudinal wave can also travel in solids, liquids and gasses because it does not depend on the shear strength of the medium it is travelling in, if that medium is like a liquid then ti does not have enough shear strength to support the oscillations, and so transverse waves cannot travel in liquids or gasses</p><p> However, longitudinal waves cannot travel throguh vacuums because there is no particles to bump into each other</p></div>"
    return f"{x}{di}"

@home.route('/test')
def test():
    return render_template('test.html')

@home.route('/testphp')
def test_php():
    return render_template('testphp.html')

@home.route("/<name>")
def user(name):
    if is_integer_num(name):
        return f"Your int squared = {name**2}"
    else:
        return render_template('name.html', content=f"{name}")

@home.route('/loops')
def loops():
    return render_template('anothertest.html')

@home.route('/snake')
@home.route('/snakegame.html')
def snake():
    return render_template('snakegame.html')

@login_required
@home.route("/snake/addleaderboard")
def add_to_snake_leader_board():
    if current_user.is_authenticated: 
        currenuserid = current_user.id
        score = request.args.get("score")
        food = request.args.get("food")
        name = current_user.name
        new = Snake_leaderboard(score=score, food=food, user_id=currenuserid, name=name)
        db.session.add(new)
        db.session.commit()
        return redirect("/dashboard")


@home.route("/snake/leaderboard")
def snake_leadeerboard():
    leaders = Snake_leaderboard.query.order_by(Snake_leaderboard.score)[::-1]
    return render_template("snakeleaderboard.html", leaders=leaders)

@home.route('/505')
def error():
    return "You stupid bugger, go fix this now"

@home.route('/resonance')
def resonance():
    return render_template('resonance.html')

@home.route('/math/square/<number>')
def square(number):
    try:
        return f"Your number squared is {float(number)**2}"
    except Exception as e:
        return e

@home.route('/math/add/<number>')
def add_num(number):
    try:
        x = [x for x in number]
        return sum(x)
    except:
        return f"Cannot calculate {number} please make it a list"

@home.route('/math/quadfinder/<lofquadpoints>')
def findthisquadeq(lofquadpoints):
    try:
        x = lofquadpoints[:2]
        y = lofquadpoints[3:]
        z = coefficient(x, y)
        aa = z[0]
        bb = z[1]
        cc = z[2]
        return f"{aa}x^2 + {bb}x + {cc}"
    except:
        return "Could not compute"

@home.route('/math/factorial/<number>')
def factorial(number):
    try:
        x = 1
        for i in int(number):
            x = x*i
        return x
    except:
        return "You must try with an integer"  

@home.route('/chemistry/periodic-table')
def periodic_table():
    return render_template("periodictable.html")

#@home.route("/admin/login", methods=["POST", "GET"])
#def login():
    #if request.method == "POST":
        #user = request.form["nm"]
        #return redirect(url_for("admin/user", usr=user))

#@home.route("/admin/<usr>")
#def user(usr):
    #return f"<h1>{usr}</h1>"

@home.route('/minesweeper')
def minesweeper():
    return render_template('minesweeper.html')

@home.route('/history')
def history():
    return "Coming soon!"

@home.route("/geography")
def geography():
    return "Coming soon!"

@home.route("/api")
def api_welcome():
    return "Hello this is the official api"

@home.route('/emailer', methods=["POST", "GET"])
def emailer():
    if request.method == "POST":
        try:
            Email = request.form["Email"]
            x = send_email(Email)
            if x == "Success":
                return "Sent the email successfully, please do not spam me"
            else:
                return x
        except:
            return f"Did not work properly, are you sure you meant to send it to {Email}"
    else:
        return render_template('emailer.html')
        
@home.route('/math/fibonacci', methods=["POST", "GET"])
def fibonnaci():
    if request.method == "POST":
        x = request.form["Fibnum"]
        y = fib(x)
        return render_template('fibonacci.html', fibnums=y)
    else:
        return render_template('fibonacci.html')

@home.route('/math/permutate', methods=["POST", "GET"])
def permutate():
    if request.method == "POST":
        y = request.form["permutations"]
        haha = list(permutations(y))
        return render_template("permutations.html", permutations=haha, len=len(haha))
    else:
        return render_template('permutations.html')

@home.route('/math/permutate/unique', methods=["POST", "GET"])
def unique_permutate():
    if request.method == "POST":
        li = []
        y = request.form["permutations"]
        haha = list(permutations(y))
        for perm in haha:
            if perm in li:
                pass
            else:
                li.homeend(perm[::-1])
        
        return render_template("permutations.html", permutations=li, len=len(li))
    else:
        return render_template('permutations.html')

# @home.route("/files/get")
# def send_randomfile():
#         x = os.listdir("/Users/mohuasen/prev/all/Armaan/PDFS")
#         file = random.choice(x)
#         try:
#             return send_file(file)
        # except Exception as e:
            # return e

@home.get("/blog")
def blog_home():
    return "A blog"

@home.errorhandler(404)
def error():
    return "This content doesn't seem to be available, sorry about that"

@home.route("/math/numberguesser")
def number_guesser():
    return render_template('numberguesser.html')

@home.route("/calculators/temperature")
def convert_temp():
    return render_template("temperature.html")

@home.get("/calculators/stopwatch")
def stopwatch():
    return render_template("stopwatch.html")

@home.route("/bloger/add", methods=["POST", "GET"])
def bog_add():
    if request.method == "POST":
        x = request.form["title"]
        cmd = f" cd ./templates && touch {x}.html"
        os.system(cmd)
        y = request.form["content1"]
        z = y.split(". ")
        with open(f"{x}.html") as file:
            file.write('{% extends "baseblog.html" %} \n')
            file.write('{% block title %}' + x + '{% endblock %}')
            file.write('{% block content%}')
            for i in z:
                file.write(f"<p>{i}</p>")
            file.write("{% endblock %}")
            file.close()
    return render_template("blogadd.html")

@home.route("/about")
def about():
    return "Hi there this is a website"

@home.route("/calculators/location")
def calc_location():
    if request.method == "POST":
        x = request.form["O"]
        z = x.split()
        xx = Position("x", z[0], z[1])
        y = request.form["N"]
        a = y.split()
        aa = Position("y", a[0], a[1])
        s = xx.distance_to(aa)
        return render_template("locations.html", d=s)
    else:
        return(render_template("locations.html"))

@home.route("/ecenomics/ftse100")
def ret_ftse100():
    b = get_ecenomic_stuff()
    return f"Ftse currently at {b[1]} points"

@home.route("/ecenomics/sandp500")
def ret_sandp500():
    b = get_ecenomic_stuff()
    return f"S&P 500 surrently at {b[2]} points"

@home.route("/ecenomics/TSLA")
def TSLA():
    b = get_ecenomic_stuff()
    return f"Tesla market cap: ${b[4]}"

@home.route("/admin/views")
def how_many_views_page():
    x = 0
    with open("views.txt", "r+") as views:
        x = int(views.read())
        x += 1
     
    with open("views.txt", "w") as views:    
        views.write(str(x))
    
    return f"this page has been viewd {x} times"

@home.route("/physics/vectors")
def vector_stuff():
    pass 
    # Can't be bothered to do the webpage for now

@home.route("/covid")
def covid():
    return "Codvid"

@home.route("/physics/gold-leaf-electroscope")
def gold_leaf_electroscope():
    return 0

@home.route("/chemistry/group1")
def alkaline_earth_matals():
    return 0

@home.route("/chemistyr/reaction-with-water")
def reaction_with_water():
    return 0

@home.route("/docs")
def docs():
    return "This is the official  documentation"

@home.route("/conway-game-life")
def conway_game_of_life():
    return "I am working on it"

@home.route("/me/files")
def file_sorter():
    y = []
    dir = request.args.get("dir", default="./files")
    dest = "/Users/mohuasen/prev/all/Armaan/PDFS"
    try:
        x = os.listdir(dir)
        for file in x:
            y.homeend(f"<li><a href='{dir}{file}' download>{file}</a></li>")
            try:
                if file.endswith(".pdf"):
                    shutil.move(f"{dir}/{file}", dest)
            except:
                continue
        
        return f"<ul>{y}</ul>"
    except Exception as e:
        return f"something went wrong: {e}"

# @home.route("/stream")
# def stream():
#     video = cv2.VideoCapture(0)
#     def generator(webcam):
#         while True:
#             success, image = video.read()
#             if success:
#                 ret, jpeg = cv2.imencode('.jpg', image)
#                 frame = jpeg.tobytes()
#                 yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
#     return Response(generator(video),mimetype='multipart/x-mixed-replace; boundary=frame')
# STUPID VERCEL THINKA OPEN-CV IS TOO LARGE

@home.route("/ip-address")
def ip_address():
    x = get_user_ip_address()
    return f"Your ip address is {x}"

@home.route("/quizzes")
def quizzes_home():
    return "I will get to as many as I can"

@home.route("/quizzes/test")
def quizzes_test():
    pass

@home.route("/bored")
def i_am_bored():
    x = Randomz.get()
    return "here is somehting: {x}"

@home.route("/api/day-of-the-year")
def day_of_year():
    x = get_day_of_the_year()
    return x

@home.route("/api/test/simpleparams")
def with_parameters():
    name = request.args.get('name')
    age = request.args.get('age', default=4)
    return jsonify(message="My name is " + name + " and I am " + str(age) + " years old")

@home.route("/api/test/question")
def test_of_question():
    x = ''
    subject = request.args.get("subject")
    topic = request.args.get("topic")
    question = request.args.get("q")
    if question.lower() == "help":
        x = "Please go to /docs"
    else:
        x = 'test'
    return jsonify({subject: {topic: {question: x}}})

@home.route("/api/sendemail")
def api_email():
    adress = request.args.get("adress")
    x = send_email(adress)
    return jsonify(status=x)

@home.route("/api/math/fibonacci")
def api_fibonacci():
    num = request.args.get("limit")
    try:
        x = fib(int(num))
        dict = {}
        for i in range(len(x)):
            dict[i] = x[i]
        return jsonify(dict, x)
    except:
        return jsonify(error='Must be integer')

@home.route("/api/math/generatepi")
def show_gen_π():
    num = int(request.args.get("accuracy"))
    x = generateπfrom_random(num)
    π = math.pi
    difference = π - x
    percentoff = 100 - (x / π)*100
    return jsonify(guess=x, actual=π, difference=difference, percenterror = percentoff, tip='Try 1000')

@home.route("/api/test/numberguesser")
def number_guesser_api():
    num = int(request.args.get("guess"))
    x = random.randint(0, 100)
    if num == x:
        return jsonify(number=num, correct=True)
    else:
        return jsonify(number=num, correct=False, actual=x)

@home.route("/api/math/collatz")
def collatz_api():
    num = int(request.args.get("number"))
    try:
        x = collatz(num)
        dict = {}
        for i in range(len(x)):
            dict[i] = x[i]
        return jsonify(dict, x)
    except:
        return jsonify(message="Must be an integer")

@home.route("/test/ipad")
def ipad_test():
    return "This is so cool"

@home.route("/mr-beast")
def mr_beast():
    return "<p>Congrats on 100 mil mr beast!!!!!!!!!!!!!!!!!!</p> <a href='https://www.youtube.com/watch?v=tVWWp1PqDus' mr</a>"

@home.route("/hs2")
def hs2():
    return "I like hs2"

@home.route("/crossrail")
def crossrail():
    return "I like crossrail"

@home.route("/other/break-my-computer")
def break_computer():
    x = (i for i in range(9999999))
    return jsonify(list(x))

@home.route("/other/devies-on-my-network")
def devices_Non_my_network():
    command = "arp -a"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return f"outputs: {output.decode('utf-8')}, errors: {error.decode('utf-8')}"

@home.route("/help/api")
def api_help_stuff():
    return "It like breaking"

@home.route("/api/test/poststuff", methods=["GET", "POST"])
def test_of_post_stuff():
    try:
        # if request.headers['Content-Type'] == 'homelication/json':
        if request.method == "POST":
            data = request.get_json()
            return jsonify(data)
        return jsonify(error="wrong method")
    except Exception as e:
        print(e)
        return jsonify(error="Error!")

@home.route("/me/why?")
def why_does_this_not_work():
    return "this should never be seen"

@home.route("/me/ipad/test")
def ipad_test_thingy_for_me():
    return "hi this was done on an ipad!!!!"

@home.route("/games/minecraft")
def minecraft():
    return "Minecraft is a very popular game it is now owned by microsoft"

@home.route("/games/crossy-roads")
def crossy_roads():
    return "I got 40,000 once, cool right? its a popular game for mobile"

@home.route("/info")
def info_stuff():
    x = get_user_ip_address()
    y = get_loc_from_ip(x)
    return "Its broken at the moment sorrry"#f"city: {y[0]}, country: {y[2]}, location: {y[3]}, postal address: {y[5]}, don't sue me you came here for a reason"

@home.route("/inflation")
def inflation_is_preety_bad():
    x = get_loc_from_ip(get_user_ip_address())
    if x[2] == "GB" or "UK":
        y = 9.4
        return f"You are in the U.K inflation pretty bad, its {y} fro cpi"
    else:
        return "I am working on getting the latest thing for you, inflation pretty bad for you unless you in japan, everyone likes japan though unless your KIM JON UN, then maybe not, but you probably not him"

@home.route("/youtube")
def youtube():
    return """
    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Youtube</a>
    <p> click it </p>
    <div>
    <summary>click it</summary>
    <article>I said click it</article>
    </div>
    <p> Enter stuff if you are bored, i am because i am</p>
    <input type="text" />
    <p> Hi youtube </p>
    <p> who am i kidding </p>
    <p> no ones gonna see this </p>
    <img src="/hello.jpeg" alt="hi">
    <p> Thats a picture </p>
    """

@home.route("/api/rrrrrr")
def rrrrrr():
    return jsonify(message="why you a pirate")

@home.route("/world")
def wrold_is_mad():
    return "it is mad"

@home.route("/ios")
def ios():
    return "It costs a lot of money"

@home.route("/android")
def android():
    return "it also costs money"

@home.route("/todosvelte")
def wierd_todo_view():
    return {"members": ["member1", "member2", "member3"]}

@home.route("/todosvelte/<path:path>")
def wierd_todo(path):
    return send_from_directory('svelte/todo', path)

@home.route("/quizzes/simple", methods=["GET", "POST"])
def quizzes_simple():
    if request.method == "POST":
        awnsers = ["hi", "test"]
        guesses = []
        dif = {}
        a = request.form.get('a')
        b = request.form.get('b')
        guesses.homeend(a)
        guesses.homeend(b)
        
        for i in range(len(awnsers)):
            if awnsers[i] != guesses[i]:
                dif[guesses[i]] = awnsers[i]
        
        return dif

@home.route("/python")
def python_explainer():
    return "I built this website with it."