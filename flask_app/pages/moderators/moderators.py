from flask import Blueprint, redirect, url_for, request, render_template
from models.user import User
from models.moderator import Moderator
from models.types import Types
from pages.forms import ModerTypes
from database import db

moderators_bp = Blueprint('moderators', __name__, template_folder='templates')


@moderators_bp.route('/moderators', methods=['GET', 'POST'])
def moderators():
    users = db.session.query(Moderator, User).join(User, Moderator.userId == User.id, isouter=True)
    types = db.session.query(Types).all()
    list_types = [(t.id, t.type) for t in types]
    form = ModerTypes()
    if request.method == "POST":
        moderator = db.session.query(Moderator).filter(Moderator.id == request.form.get("moder_id")).first()
        moderator.role = request.form.get("role_id")
        db.session.add(moderator)
        db.session.commit()
        return redirect(url_for('moderators.moderators'))
    users = db.session.execute(users)
    return render_template('moderators.html', users = users, list_types=list_types)
