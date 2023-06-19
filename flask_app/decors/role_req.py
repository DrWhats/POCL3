from functools import wraps
from flask import g, request, redirect, url_for, flash, session
from database import db
from models.moderator import Moderator
from models.user import User


def role_req(role_id):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not session.get("user_id"):
                flash('У вас недостаточно прав для доступа к этой странице.', 'danger')
                return redirect(url_for('index.index'))
            else:
                user = (db.session.query(Moderator, User).
                        join(User, Moderator.userId == session["user_id"], isouter=True)).first()
                if user.Moderator.role == role_id:
                    return redirect(url_for('index.index'))
                return f(*args, **kwargs)
        return decorated_function

    return decorator
