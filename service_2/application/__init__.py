from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('SFIA2_DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def home(id):
    # food = request.args.get("food")
    # print(food)
    rand = random.randint(1, 10)
    getCuisine = Western.query.filter_by(id=rand).first()
    return getCuisine
    
