from flask import render_template, session, url_for, redirect, request, Blueprint, flash
from database import db
from pages.forms import QuestionsForm
from models.request import Request
from models.types import Types
from classifier.classifier import predict
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

        new_request = Request(
            fio=fio,
            phone_number=phonenumber,
            type_id=None,
            shortdescribe=shortdescribe,
            question=question 
        )

        db.session.add(new_request)
        db.session.commit()
        question_type = predict(question)
        print(question_type)
        type_id = db.session.query(Types.id).filter(Types.type == question_type)
        query = db.session.query(Request).filter(Request.question == question).update({Request.typeId: type_id})
        print(query)
        return render_template('question_success.html')
    else:
        flash("Invalid username or password.", 'error')
    return render_template('question.html', form = form)
