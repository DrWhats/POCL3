from database import db
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash


class Moderator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(User.id), unique=True, nullable=True)
    role = db.Column(db.String(15), unique=False, nullable=True)
    tg = db.Column(db.String(15), unique=True, nullable=True)

    def __init__(self, id, userId, role, tg):
        self.id = id
        self.userId = userId
        self.role = role
        self.tg = tg

    def __repr__(self):
        return f'<Moderator {self.id}, {self.tg}, {self.role}>'