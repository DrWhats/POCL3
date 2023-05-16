from flask import render_template, session, url_for, redirect, request, Blueprint, flash
from models.user import User
import database
from werkzeug.security import generate_password_hash
from pages.forms import QuestionsForm
blueprint = Blueprint('index', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = QuestionsForm()
    if form.validate_on_submit():
        fio = form.fio.data
        email = form.email.data
        phonenumber = form.phonenumber.data
        shortdescribe = form.shortdescribe.data
        question = form.question.data
        print(fio)
        print(email)
        print(phonenumber)
        print(shortdescribe)
        print(question)
        return redirect(url_for('index.index'))
    else:
        flash("Invalid username or password.", 'error')
    return render_template('question.html', form = form)
