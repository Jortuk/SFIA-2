from application import db
from application.models import Drink

db.drop_all()
db.create_all()