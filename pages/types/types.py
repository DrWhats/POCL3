from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from pages.forms import TypeForm
from models.types import Types
from database import db

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
