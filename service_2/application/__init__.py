from flask import Flask, request
from random import choice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def service2():
    western_cuisine = ["American", "British", "Caribbean", "French", "Greek", "Italian", "Mediterranean", "Mexican", "Moroccan", "Spanish"]
    eastern_cuisine = ["Chinese", "Indian", "Japanese", "Thai", "Turkish", "Vietnamese", "Arabian", "Kurdish", "Lebanese", "Syrian"]
    food = request.args.get("food")
    print(food)
    if food == "western":
        cuisine = choice(western_cuisine)
    else:
        cuisine = choice(eastern_cuisine)
    return cuisine