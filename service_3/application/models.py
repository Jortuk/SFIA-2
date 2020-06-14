from application import db

class Dessert(db.Model):
    __tablename__ = 'dessert'
    id = db.Column(db.Integer, primary_key=True)
    dessert = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return str(self.dessert)