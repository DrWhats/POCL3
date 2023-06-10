from flask import Blueprint, redirect, url_for, request, render_template
from flask_app.models.user import User
from flask_app.models.moderator import Moderator
from flask_app.models.types import Types
from flask_app.pages.forms import ModerTypes
from flask_app.database import db

moderators_bp = Blueprint('moderators', __name__, template_folder='templates')


@moderators_bp.route('/moderators', methods=['GET', 'POST'])
def moderators():
    user = db.session.query(Moderator, User).join(User, Moderator.id == User.userId, isouter=True)
    types = db.session.query(Types).fetchall()
    for row in types:
        print(row.id)
        print(row.type)
    form = ModerTypes()
    if form.validate_on_submit():
        moderator = Moderator(user_id=form.user_id.data, role=1)
        moderator.role = form.dropdown.data
        db.session.add(moderator)
        db.session.commit()
        return redirect(url_for('moderators.moderators'))
    users = db.session.execute(user)
    return render_template('moderators.html', users = users, form=form)
