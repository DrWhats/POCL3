from database import db
from models.user import User
from models.types import Types
from models.moderator import Moderator


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    fio = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    typeId = db.Column(db.Integer, db.ForeignKey(Types.id), nullable=False)
    phoneNumber = db.Column(db.String(12), nullable=False)
    moderatorId = db.Column(db.Integer, db.ForeignKey(Moderator.id), nullable=False)
    shortdescribe = db.Column(db.String(50), nullable=False)
    question = db.Column(db.String(50), nullable=False)
    

    def __init__(self, userId, fio, email, typeId, phoneNumber, moderatorId, shortdescribe, question):
        self.userId = userId
        self.fio = fio
        self.email = email
        self.typeId = typeId
        self.phoneNumber = phoneNumber
        self.moderatorId = moderatorId
        self.shortdescribe = shortdescribe
        self.question = question

    def __repr__(self):
        return f'<Request {self.userId}, {self.typeId}, {self.comment}>'
