import requests
from bs4 import BeautifulSoup
from math import asin, cos, radians, sin, sqrt, tan
import cmath
import math
import random
from flask import request, jsonify
import datetime
import smtplib
import ssl
from email.message import EmailMessage
from flask_mail import Mail, Message
from . import mail
import requests

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def bmi(weigth, height):
    x = weigth / height ** 2
    return x

def area_based_on_sides(sides, length):
    if sides == 1:
        area = math.pi * length**2
        return area
    elif sides == 2:
        return length
    elif sides == 3:
        s = (length * 3) / 2
        a = s*(s-length)*(s-length)*(s-length)
        return a**0.5
    elif sides == 4:
        return length**2
    elif sides == 5:
        x = (5*(5 + 2*(5**0.5)))
        return (1/4)*x*length**2
    elif sides == 6:
        x = 3*(3**0.5)
        return (x/2) * length**2
    elif sides % 2 == 1:
        x = (sides/4)*length**2
        a = 1/(tan(180/sides))
        return x*a
    elif sides == 8:
        x = 2*(1 + 2**0.5)*length**2
    elif sides == 10:
        x = (5/2)*length**2
        a = (5 + 2*(5**0.5))**0.5
        return x*a
    else:
        return math.pi*length**2
    

def coefficient(x,y):
    x_1 = x[0]
    x_2 = x[1]
    x_3 = x[2]
    y_1 = y[0]
    y_2 = y[1]
    y_3 = y[2]

    a = y_1/((x_1-x_2)*(x_1-x_3)) + y_2/((x_2-x_1)*(x_2-x_3)) + y_3/((x_3-x_1)*(x_3-x_2))

    b = (-y_1*(x_2+x_3)/((x_1-x_2)*(x_1-x_3))
         -y_2*(x_1+x_3)/((x_2-x_1)*(x_2-x_3))
         -y_3*(x_1+x_2)/((x_3-x_1)*(x_3-x_2)))

    c = (y_1*x_2*x_3/((x_1-x_2)*(x_1-x_3))
        +y_2*x_1*x_3/((x_2-x_1)*(x_2-x_3))
        +y_3*x_1*x_2/((x_3-x_1)*(x_3-x_2)))

    return a,b,c

def generateπfrom_random(n):
    ins = 0
    total = 0
    for i in range(n):
        x = random.randint(0, 1)
        y = random.randint(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            ins += 1
        total +=1
    
    return 4*ins/total

def trajectory(vx, vy, h):
    # y = h + x * tan(α) - g * x² / (2 * V₀² * cos²(α))
    g = 9.80665
    l = vx * sqrt(vy**2 + 2*g*h)
    x = [i for i in range(10)]

def quadratic_solver(a, b, c):
    deter = b**2 - (4*a*c)
    if deter >= 0:
        x = (-b + sqrt(deter))/(2*a)
        y = (-b - sqrt(deter))/(2*a)
        return [x, y]
    else:
        x = (-b + cmath.sqrt(deter))/(2*a)
        y = (-b - cmath.sqrt(deter))/(2*a)
        return [x, y]

def cubic_solver(a, b, c, d):
    # Because I am bored
    x = ((-1*b**3)/27*a**3) + ((b*c)/6*a**2) - d/2*a
    deter = x**2 + ((c/3*a) - (b**2)/(9*a**2))**3
    if deter >= 0:
        f = ((x + sqrt(deter))**(1/3)) + ((x - sqrt(deter))**(1/3)) - b/3*a
        return f
    else:
        f = ((x + cmath.sqrt(deter))**(1/3)) + ((x - cmath.sqrt(deter))**(1/3)) - b/3*a
        return f

def get_top_bbc_news():
    URL = "https://www.bbc.co.uk/news"

    response  = requests.get(URL)

    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find_all("span", "gs-c-promo-heading__title gel-pica-bold")

    x = []

    for i in result:
        x.append(i.text)

    return x[-10:]

# def cpp_generate_π():
    # lib = cdll.LoadLibrary('./c++/runner.o')
    # print(lib)

# cpp_generate_π()

def get_top_bbc_links():
    URL = "https://www.bbc.co.uk/news"
    response2  = requests.get(URL)
    z = []

    soup2 = BeautifulSoup(response2.content, "html.parser")
    result2 = soup2.find_all("a", {'class': "gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs"})

    for i in result2:
        x = i.get("href")
        z.append(x)
    
    return z

def get_top_bbc_content():
    x = get_top_bbc_links()
    l = []
    for i in range(len(x)):
        URL = f"https://www.bbc.co.uk{x[i]}"
        response = requests.get(URL)
        y = []
        soup = BeautifulSoup(response.content, "html.parser")
        try:
            result = soup.find_all("p", "ssrcss-ugte5s-Contributor e5xb54n2")
            y.append(result[0].text)
        except:
            y.append("Could not get author")
        ro = soup.find_all("time")
        y.append(ro[0].text)
        l.append(y)
 
    
    return l

def get_top_bbc_actual():
    x = get_top_bbc_links()
    l = []
    for i in range(len(x)):
        URL = f"https://www.bbc.co.uk{x[i]}"
        response = requests.get(URL)
        try:

            soup = BeautifulSoup(response.content, "html.parser")
            result = soup.find_all("article", "ssrcss-pv1rh6-ArticleWrapper")
            l.append(result[0].text)
        except:
            l.append("coud not be found")
    
    return l

def get_world_covid():
    URL = "https://www.worldometers.info/coronavirus/"

    x = []

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    result = soup.find_all("div", "maincounter-number")
    x.append(result[0].text)
    x.append(result[1].text)
    x.append(result[2].text)
    return x

def get_country_covid(country):
    x = []
    URL = f"https://www.worldometers.info/coronavirus/country/{country}"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    result = soup.find_all("div", "maincounter-number")
    x.append(result[0].text)
    x.append(result[1].text)
    x.append(result[2].text)
    return x

def get_ecenomic_stuff():
    stuff = []
    # GBP TO EUR
    URL = "https://www.bbc.co.uk/news/topics/cx250jmk4e7t/pound-sterling-gbp"
    response = requests.get(URL)

    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find_all("div", class_="gel-paragon nw-c-md-currency-summary__value")
    stuff.append(result[0].text)

    # FTSE 100

    URL2 = "https://www.bbc.co.uk/news/topics/c9qdqqkgz27t/ftse-100"
    response2 = requests.get(URL2)

    soup2 = BeautifulSoup(response2.content, "html.parser")
    result2 = soup2.find_all("div", class_="gel-paragon nw-c-md-market-summary__value")
    stuff.append(result2[0].text)

    # S&P 500
    URL3 = "https://www.bbc.co.uk/news/topics/c4dldd02yp3t/sp-500"
    response3 = requests.get(URL3)

    soup3 = BeautifulSoup(response3.content, "html.parser")
    result3 = soup3.find_all("div", class_="gel-paragon nw-c-md-market-summary__value")
    stuff.append(result3[0].text)

    # GOOGLE FINANCE SCRAPING AAPL
    URL4 = "https://www.google.com/finance/quote/AAPL:NASDAQ"
    response4 = requests.get(URL4)

    soup4 = BeautifulSoup(response4.content, "html.parser")
    result4 = soup4.find_all("div", class_="YMlKec fxKbKc")
    stuff.append(result4[0].text)

    # GOOGLE FINANCE TSLA

    URL5 = "https://www.google.com/finance/quote/TSLA:NASDAQ"
    response5 = requests.get(URL5)

    soup5 = BeautifulSoup(response5.content, "html.parser")
    result5 = soup5.find_all("div", class_="P6K39c")
    stuff.append(result5[0].text)

    return stuff

def get_user_ip_address():
    if 'X-Forwarded-For' in request.headers:
        ip_address = str(request.headers['X-Forwarded-For'])
    else:
        ip_address = str(request.environ.get('HTTP_X_REAL_IP',
                         request.remote_addr))

    if ip_address == '127.0.0.1':
        ip_address = requests.get('http://ipecho.net/plain')
        if ip_address.status_code != 200:
            ip_address = requests.get('http://ip.42.pl/raw')
        ip_address = ip_address.text
    ip_address = ip_address.split(",")[0]
    return ip_address

def get_loc_from_ip(ip):
    x = requests.get(f"https://ipinfo.io/{ip}")
    a = x["city"]
    b = x["region"]
    c = x["country"]
    d = x["loc"]
    e = x["org"]
    f = x["postal"]
    
    z = [a, b, c, d, e, f]
    return z

def fib(num): 
    result = []
    count = 0
    n1 = 0
    n2 = 1
    while count < int(num):
       result.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
    return result


# DO THIS
# 
# 
# 
def collatz(num):
    x = []
    while num > 1:
        if num % 2 == 0:
            num = num / 2
            x.append(num)
        else:
            num = num*3 + 1
            x.append(num)
    
    return x
# 
# 
# 

def get_day_of_the_year():
    days = 0
    year = datetime.now().year
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days = 366
    else:
        days = 365
    days_passed_year = datetime.now().timetuple().tm_yday
    return jsonify(time=datetime.now() , days_total=days , days_passed=days_passed_year , days_to_go=(days-days_passed_year) )


def send_email(address):
    try:
        sender_email = "drive.banerjee.armaan@gmail.com"
        receiver_email = address
        if address.endswith("orange.fr"):
            return "no"
        x = [i for i in address]
        y = x.count("@")
        if "." not in x and y != 1:
            return "wrong address sorry"
        password = "ixsrblyncyrupttv"
        message = EmailMessage()
        subject = "HI there"
        body = f"Hello there, you have been emailed from me, your email adress is {address}"
        x = get_ecenomic_stuff()
        l = x[0]
        body2 = f"The GBP is worth €{l}"
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        html = f"""
        <html>
            <body>
                <h1>{subject}</h1>
                <br>
                <p>{body}</p>
                <p>{body2}</p>
                <img src="./hello.jpeg" alt="hello image">
            </body>
        </html>
        """

        message.add_alternative(html, subtype="html")

        context = ssl.create_default_context()


        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        return "Success"
    except Exception as e:
        return e

def send_newsletter_with_flask(title, addresses, content):
    msg = Message(f"{title}", sender="drive1.banerjee.armaan@gmail.com", recipients=addresses)
    msg.html = content
    mail.send(msg)
    return "sent"

def send_email_newsletter(address, content):
    try:
        sender_email = "drive.banerjee.armaan@gmail.com"
        receiver_email = address
        password = "ixsrblyncyrupttv"
        message = EmailMessage()
        subject = "Newsletter"
        body = f"Hello there, you have been emailed from me, your email adress is {address}"
        x = get_ecenomic_stuff()
        l = x[0]
        body2 = f"The GBP is worth €{l}"
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        now_date = datetime.now()

        html = f"""
        <html>
            <body>
                <h1>{subject}</h1>
                <br>
                <p>{body}</p>
                <p>{body2}</p>
                <div>
                <p>{content}</p>
                </div>
                <p>Armaan Banerjee - {now_date}</p>
            </body>
        </html>
        """

        message.add_alternative(html, subtype="html")

        context = ssl.create_default_context()


        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        return "Success"
    except Exception as e:
        return e

def convert_currency(amount, currency: str):
    URL = "https://cdn.moneyconvert.net/api/latest.json"
    response = requests.get(URL)
    rate = response.json()["rates"][currency]
    if rate:
        act = amount / rate
        return f"${act}"