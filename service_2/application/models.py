from application import db

class Food(db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return str(self.food)