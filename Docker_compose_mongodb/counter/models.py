from app import db

class Counter(db.Document):
    count = db.IntField(db_field = 'c')