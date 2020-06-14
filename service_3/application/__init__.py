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

from application.models import Dessert  

@app.route('/', methods=['GET', 'POST'])
def dessert():
    rand = random.randint(1, 20)
    getDessert = Dessert.query.filter_by(id=rand).first()
    print(getDessert)
    return str(getDessert)