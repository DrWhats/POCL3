import os

from flask_sqlalchemy import SQLAlchemy
from models.moderator import Moderator
from models.request import Request
from models.types import Types
from models.user import User

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
    db.init_app(app)
    with app.app_context():
        db.create_all()
        print("Created Tables")
