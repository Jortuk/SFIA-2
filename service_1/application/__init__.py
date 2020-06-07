from flask import Flask, request, render_template
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

@app.route('/', methods=['GET'])
@app.route('/home')
def home():
    mealData = Meals.query.all()
    meal = requests.get("http://service_4:5004/output").text
    return render_template('home.html', title = 'RMG', meals = mealData)
