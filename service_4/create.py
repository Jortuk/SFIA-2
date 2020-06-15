from application import db
from application.models import Chow


db.drop_all()
db.create_all()