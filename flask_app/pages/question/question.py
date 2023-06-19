import requests
from database import db
from flask import Blueprint, flash, render_template
from models.request import Request
from models.types import Types
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

        new_request = Request(
            fio=fio,
            email=email,
            phone_number=phonenumber,
            type_id=None,
            shortdescribe=shortdescribe,
            question=question 
        )

        db.session.add(new_request)
        db.session.commit()
        luboy_slovarik = {"question": question, "email": email, "phone_number": phonenumber, "fio": fio}
        response = requests.post(url="http://10.5.0.5:8000/model_request",
                                 json=luboy_slovarik,
                                 headers={"Content-Type": "application/json"})
        print(response.status_code)
        print(response.text)
        return render_template('question_success.html')
    else:
        flash("Invalid username or password.", 'error')
    return render_template('question.html', form = form)
