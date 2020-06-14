from application import db
from application.models import Cuisine

db.drop_all()
db.create_all()