from flask import Blueprint, redirect, url_for, session
from flask_login import logout_user


logout_bp = Blueprint('logout', __name__, template_folder='templates')


@logout_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('index.index'))
