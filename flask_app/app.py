from flask import Flask
from datetime import timedelta
from pages.index import index
from pages.login import login
from pages.register import register
from pages.question import question
from pages.logout import logout
from pages.users import users
from pages.about import about
from pages.admin import admin
from pages.types import types
from pages.type_moderator import type_moderator
from pages.moderators import moderators
from database import init_db
from models.user import User
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__, template_folder='pages/base/templates')
app.config['SECRET_KEY'] = 'secret-key'
app.permanent_session_lifetime = timedelta(minutes=30)
init_db(app)
login_manager.init_app(app)

app.register_blueprint(index.blueprint)
app.register_blueprint(login.login_bp)
app.register_blueprint(register.register_bp)
app.register_blueprint(question.question_bp)
app.register_blueprint(logout.logout_bp)
app.register_blueprint(users.users_bp)
app.register_blueprint(about.about_bp)
app.register_blueprint(admin.admin_bp)
app.register_blueprint(types.types_bp)
app.register_blueprint(moderators.moderators_bp)
app.register_blueprint(type_moderator.type_moderator_bp)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
