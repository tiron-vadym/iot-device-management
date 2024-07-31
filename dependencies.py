from app.database import db
from app.models import ApiUser, Location, Device


def init_db():
    db.connect()
    db.create_tables([ApiUser, Location, Device])
    db.close()
