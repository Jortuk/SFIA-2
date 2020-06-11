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

from application.models import Cuisine

@app.route('/', methods=['GET', 'POST'])
def cuisine():
    rand = random.randint(1, 20)
    getCuisine = Cuisine.query.filter_by(id=rand).first()
    print(getCuisine)
    return str(getCuisine)