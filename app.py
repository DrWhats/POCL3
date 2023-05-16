from flask import Flask
from flask_login import LoginManager
from datetime import timedelta
from pages.index import index
from pages.login import login
from pages.register import register
from pages.question import question
from pages.logout import logout
from pages.users import users
from database import init_db, db
from models.user import User
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__, template_folder='pages/base/templates')
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=30)
init_db(app)
login_manager.init_app(app)

app.register_blueprint(index.blueprint)
app.register_blueprint(login.login_bp)
app.register_blueprint(register.register_bp)
app.register_blueprint(question.question_bp)
app.register_blueprint(logout.logout_bp)
app.register_blueprint(users.users_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
