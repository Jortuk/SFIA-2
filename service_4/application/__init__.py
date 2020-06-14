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

from application.models import Chow

@app.route('/', methods=['GET', 'POST'])
def chow():
    cuisine = requests.get("http://service2:5002/").text
    dessert = requests.get("http://service3:5003/").text
    output = Chow(
        cuisine = cuisine,
        dessert = dessert
    )
    db.session.add(output)
    db.session.commit()
    return "Your cuisine is " + cuisine + ", and your dessert is " + dessert + "!"