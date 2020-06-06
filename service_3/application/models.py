from application import db

class Soft(db.Model):
    __tablename__ = 'soft_drinks'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'Drink: ', str(self.type)
            ])
    
    def __init__(self, id, type):
        self.id = id
        self.type = type

class Alco(db.Model):
    __tablename__ = 'alco_drinks'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'Drink: ', str(self.type)
            ])
    
    def __init__(self, id, type):
        self.id = id
        self.type = type