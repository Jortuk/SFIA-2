from application import db

class Meals(db.Model):
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(30), nullable=False)
    drink = db.Column(db.String(30), nullable=False)