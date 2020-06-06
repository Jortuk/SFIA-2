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
    food = requests.args.get("http://service_2:5001").text
    bev = requests.args.get("http://service_3:5002").text
    output = Meals(
        cuisine = food,
        drink = bev
    )
    db.session.add(output)
    db.session.commit()
    return "Your cuisine is " + food + ", and your drink is " + bev + "!"