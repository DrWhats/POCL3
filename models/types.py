from database import db


class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, id, type):
        self.id = id
        self.type = type

    def __repr__(self):
        return f'<Type {self.id}, {self.type}>'