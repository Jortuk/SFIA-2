from application import db

class Cuisine(db.Model):
    __tablename__ = 'cuisine'
    id = db.Column(db.Integer, primary_key=True)
    cuisine = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return str(self.cuisine)