from flask import render_template, session, url_for, redirect, request, Blueprint
from models.user import User
import database
from werkzeug.security import generate_password_hash

blueprint = Blueprint('index', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.get('Дисциплина'))
    return render_template('index.html')
