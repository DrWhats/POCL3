from flask import render_template, Blueprint
blueprint = Blueprint('index', __name__, template_folder='templates')


@blueprint.route('/index', methods=['GET', 'POST'])
@blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
