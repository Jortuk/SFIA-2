from application import db
from application.models import Food

db.drop_all()
db.create_all()