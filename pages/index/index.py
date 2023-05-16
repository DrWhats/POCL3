from flask import render_template, session, url_for, redirect, request, Blueprint, flash
from models.user import User
import database
from werkzeug.security import generate_password_hash
from pages.forms import QuestionsForm
blueprint = Blueprint('index', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
