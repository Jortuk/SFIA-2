from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('SFIA2_DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)

from application.models import Meals
import requests

@app.route('/output', methods=['GET', 'POST'])
def meals():
    food = requests.get("http://service_2:5002/cuisine").text
    bev = requests.get("http://service_3:5003/drink").text
    output = Meals(
        cuisine = food,
        drink = bev
    )
    db.session.add(output)
    db.session.commit()
    return "Your cuisine is " + food + ", and your drink is " + bev + "!"