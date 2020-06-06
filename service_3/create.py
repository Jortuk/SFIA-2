from application import db
from application.models import Soft, Alco

db.drop_all()
db.create_all()