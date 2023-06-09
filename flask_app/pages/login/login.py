from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from models.user import User
from pages.forms import LoginForm

login_bp = Blueprint('login', __name__, template_folder='templates')


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Welcome, you have successfully logged in.', 'success')
            login_user(user)
            return redirect(url_for('index.index'))
        else:
            flash("Invalid username or password.", 'error')

    return render_template('login.html', form=form)
