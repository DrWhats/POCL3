from flask import Blueprint, redirect, url_for, request, render_template
from models.user import User
from database import db

users_bp = Blueprint('users', __name__, template_folder='templates')


@users_bp.route('/users', methods=['GET', 'POST'])
def logout():
    # if request.method == 'POST':
    #     print(request.form.get('Дисциплина'))
    users = User.query.all()
    return render_template('users.html', users = users)
