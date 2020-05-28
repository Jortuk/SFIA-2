from flask import Flask, request
from random import choice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def service2():
    cuisine = ["American", "British", "Caribbean", "Chinese", "French", "Greek", "Indian", "Italian", 
    "Japanese", "Mediterranean", "Mexican", "Moroccan", "Spanish", "Thai", "Turkish", "Vietnamese"]
    