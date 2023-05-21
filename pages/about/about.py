from flask import render_template, Blueprint

about_bp = Blueprint('about', __name__, template_folder='templates')


@about_bp.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
