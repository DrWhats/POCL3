from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from database import db
from pages.forms import RegisterForm

register_bp = Blueprint('register', __name__, template_folder='templates')


@register_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    reg_html = 'register.html'
    if form.validate_on_submit():
        print("FORM")
        username = form.username.data
        email = form.email.data.lower()
        password = form.password.data

    
        if len(username) < 2:
            flash('Имя пользователя должно быть длиннее 1 символа', 'error')
            return render_template(reg_html, form=form)

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Имя пользователя уже занято', 'error')
            return render_template(reg_html, form=form)

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email уже занят', 'error')
            return render_template(reg_html, form=form)
        
        print(password)
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Вы успешно зарегистрировались! Теперь выполните вход.', 'success')
        return redirect(url_for('login.login'))

    return render_template(reg_html, form=form)
