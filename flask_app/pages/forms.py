from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, HiddenField, FieldList, SelectField
from wtforms.widgets import ListWidget
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Подвтердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')


class LoginForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Войти')


class QuestionsForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    question = StringField('Вопрос', validators=[DataRequired()])
    shortdescribe = StringField('Краткое описание', validators=[DataRequired(), Length(max=100)])
    fio = StringField('ФИО', validators=[DataRequired()])
    phonenumber = StringField('Номер телефона', validators=[DataRequired(), Length(min=11, max=11)])


class TypeForm(FlaskForm):
    type = StringField('Тип заявки', validators=[DataRequired()])


class ModeratorForm(FlaskForm):
    id = HiddenField(validators=[DataRequired()])
    actions = HiddenField(validators=[DataRequired()])


class ModerTypes(FlaskForm):
    user_id = HiddenField(validators=[DataRequired()])
    choices = []
    dropdown = SelectField('Выберите тип', choices=choices)
    submit = SubmitField('Сохранить')
