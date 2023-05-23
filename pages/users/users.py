from flask import Blueprint, redirect, url_for, request, render_template
from models.user import User
from models.moderator import Moderator
from pages.forms import ModeratorForm
from database import db

users_bp = Blueprint('users', __name__, template_folder='templates')


@users_bp.route('/users', methods=['GET', 'POST'])
def users():
    form = ModeratorForm()
    query = db.session.query(User, Moderator).join(Moderator, User.id == Moderator.userId, isouter=True)
    if form.validate_on_submit():
        print('SUB')
        new_moderator = Moderator(userId=form.id.data, role=1)
        db.session.add(new_moderator)
        db.session.commit()
        return redirect(url_for('users.users'))
    print(query)
    users = db.session.execute(query)
    print(users)
    return render_template('users.html', users = users, form=form)
