from application import db

class Western(db.Model):
    __tablename__ = 'western_cuisine'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'Cuisine: ', str(self.type)
            ])
    
    def __init__(self, id, type):
        self.id = id
        self.type = type

class Eastern(db.Model):
    __tablename__ = 'eastern_cuisine'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'Cuisine: ', str(self.type)
            ])

    def __init__(self, id, type):
        self.id = id
        self.type = type
