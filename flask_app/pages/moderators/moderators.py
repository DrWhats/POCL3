from database import db
from decors.role_req import role_req
from flask import Blueprint, redirect, render_template, request, url_for
from models.moderator import Moderator
from models.types import Types
from models.user import User

moderators_bp = Blueprint('moderators', __name__, template_folder='templates')


@moderators_bp.route('/moderators', methods=['GET', 'POST'])
@role_req(1)
def moderators():
    users = (db.session.query(Moderator, User, Types)
             .join(User, Moderator.userId == User.id, isouter=True)
             .join(Types, Moderator.typeId == Types.id, isouter=True))
    types = db.session.query(Types).all()
    list_types = [(t.id, t.type) for t in types]
    if request.method == "POST":
        moderator = db.session.query(Moderator).filter(Moderator.id == request.form.get("moder_id")).first()
        moderator.role = request.form.get("role_id")
        db.session.add(moderator)
        db.session.commit()
        return redirect(url_for('moderators.moderators'))
    users = db.session.execute(users)
    return render_template('moderators.html', users=users, list_types=list_types)
