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

@app.route('/cuisine', methods=['GET', 'POST'])
def western(id):
    rand = random.randint(1, 10)
    getCuisine = Western.query.filter_by(id=rand).first()
    print(getCuisine)
    return getCuisine

# @app.route('/eastern', methods=['GET', 'POST'])
# def eastern(id):
#     rand = random.randint(1, 10)
#     getCuisine = Eastern.query.filter_by(id=rand).first()
#     return getCuisine
    
