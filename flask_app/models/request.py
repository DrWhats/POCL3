from database import db
from models.user import User
from models.types import Types
from models.moderator import Moderator


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)
    fio = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    typeId = db.Column(db.Integer, db.ForeignKey(Types.id), nullable=True)
    phoneNumber = db.Column(db.String(12), nullable=False)
    moderatorId = db.Column(db.Integer, db.ForeignKey(Moderator.id), nullable=True)
    shortdescribe = db.Column(db.String(50), nullable=False)
    question = db.Column(db.String(50), nullable=False)

    def __init__(self, fio, phone_number, shortdescribe, question, user_id=None, email=None, type_id=None,
                 moderator_id=None):
        self.userId = user_id
        self.fio = fio
        self.email = email
        self.typeId = type_id
        self.phoneNumber = phone_number
        self.moderatorId = moderator_id
        self.shortdescribe = shortdescribe
        self.question = question

    def __repr__(self):
        return f'<Request {self.userId}, {self.typeId}, {self.comment}>'
