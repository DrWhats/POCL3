from database import db
from models.user import User
from models.types import Types
from models.moderator import Moderator


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(User.id))
    typeId = db.Column(db.Integer, db.ForeignKey(Types.id))
    phoneNumber = db.Column(db.String(12), nullable=False)
    moderatorId = db.Column(db.Integer, db.ForeignKey(Moderator.id))
    comment = db.Column(db.String(50), nullable=False)

    def __init__(self, userId, typeId, phoneNumber, moderatorId, comment):
        self.userId = userId
        self.typeId = typeId
        self.phoneNumber = phoneNumber
        self.moderatorId = moderatorId
        self.comment = comment

    def __repr__(self):
        return f'<Request {self.userId}, {self.typeId}, {self.comment}>'
