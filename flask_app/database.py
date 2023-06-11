from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db'
    db.init_app(app)
    with app.app_context():
        from models.user import User
        from models.types import Types
        from models.request import Request
        from models.moderator import Moderator
        db.create_all()
        print("Created Tables")
