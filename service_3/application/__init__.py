from flask import Flask, request
from random import choice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    soft_drink = ["Coke", "Diet Coke", "Orange Juice", "Apple Juice", "Still Water", "Sparkling Water", "Sprite", "Fanta"]
    alco_drink = ["Beer", "Lager", "Red Wine", "White Wine", "Rose", "Ale", "Cider", "IPA"]
    drink = request.args.get("drink")
    print(drink)
    if perk == "soft":
        bev = choice(soft_drink)
    else:
        bev = choice(alco_drink)
    return bev