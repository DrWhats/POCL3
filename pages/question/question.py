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
            email=email,
            phone_number=phonenumber,
            type_id=None,
            shortdescribe=shortdescribe,
            question=question 
        )

        db.session.add(new_request)
        db.session.commit()
<<<<<<< Updated upstream:pages/question/question.py
        question_type = predict(question)
        type_id = db.session.query(Types.id).filter(Types.type == question_type)
        current_requset = db.session.execute(db.session.query(Request).filter(Request.question == question))
        current_requset.typeId = type_id
        db.session.commit()
=======
        luboy_slovarik = {"question": question}
        response = requests.post(url="http://127.0.0.1:8000/model_request",
                                 json=luboy_slovarik,
                                 headers={"Content-Type": "application/json"})
>>>>>>> Stashed changes:flask_app/pages/question/question.py
        return render_template('question_success.html')
    else:
        flash("Invalid username or password.", 'error')
    return render_template('question.html', form = form)
