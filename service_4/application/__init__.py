from flask import Flask, request
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('SFIA2_DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)

from application.models import Meals

@app.route('/', methods=['GET', 'POST'])
def meals():
    food = requests.get("http://service2:5002/").text
    drink = requests.get("http://service3:5003/").text
    output = Meals(
        food = food,
        drink = drink
    )
    db.session.add(output)
    db.session.commit()
    return "Your food is " + food + ", and your drink is " + drink + "!"