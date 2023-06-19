from database import db
from flask import Blueprint, redirect, render_template, url_for
from models.types import Types
from pages.forms import TypeForm

types_bp = Blueprint('types', __name__, template_folder='templates')


@types_bp.route('/types', methods=['GET', 'POST'])
def types():
    form = TypeForm()
    current_types = Types.query.all()
    if form.validate_on_submit():
        type = form.type.data
        new_type = Types(type=type)
        db.session.add(new_type)
        db.session.commit()
        return redirect(url_for('types.types'))
    return render_template('types.html', form=form, current_types=current_types)
