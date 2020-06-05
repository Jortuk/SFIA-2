from application import db
from application.models import Western

db.drop_all()
db.create_all()