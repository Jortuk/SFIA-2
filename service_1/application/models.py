from application import db

class Meals(db.Model):
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True)
    cuisine = db.Column(db.String(30), nullable=False)
    drink = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'Meal: ', str(self.meal)
            ])

    def __init__(self, id, meal):
        self.id = id
        self.meal = meal