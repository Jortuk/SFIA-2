from application import db
from application.models import Dessert

db.drop_all()
db.create_all()