from application import db

class Drink(db.Model):
    __tablename__ = 'drink'
    id = db.Column(db.Integer, primary_key=True)
    drink = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return str(self.drink)