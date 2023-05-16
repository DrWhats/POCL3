from flask import render_template, session, url_for, redirect, request, Blueprint, flash
from pages.forms import QuestionsForm
question_bp = Blueprint('question', __name__, template_folder='templates')


@question_bp.route('/question', methods=['GET', 'POST'])
def question():
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
        return render_template('question_success.html')
    else:
        flash("Invalid username or password.", 'error')
    return render_template('question.html', form = form)
