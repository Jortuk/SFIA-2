from application import db

class Chow(db.Model):
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True)
    cuisine = db.Column(db.String(30), nullable=False)
    dessert = db.Column(db.String(30), nullable=False)