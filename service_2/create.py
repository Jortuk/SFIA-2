from application import db
from application.models import Western, Eastern

db.drop_all()
db.create_all()