from flask import Blueprint, redirect, url_for, request, render_template
from models.user import User
from models.moderator import Moderator
from models.types import Types
from database import db
from decors.role_req import role_req

type_moderator_bp = Blueprint('type_moderator', __name__, template_folder='templates')


@type_moderator_bp.route('/type_moderator', methods=['POST'])
@role_req(1)
def type_moderator():
    types = db.session.query(Types).all()
    list_types = [(t.id, t.type) for t in types]
    if request.method == "POST":
        if request.form.get('action') == 'open':
            sql = (db.session.query(User, Moderator)
                   .outerjoin(Moderator, Moderator.userId == User.id)
                   .filter(Moderator.id == request.form.get("moder_id")))
            user = sql.first()
            return render_template('moderator_type.html', user=user, types=list_types)
        if request.form.get('action') == 'assign':
            moderator = db.session.query(Moderator).filter(Moderator.id == request.form.get("moder_id")).first()
            moderator.typeId = request.form.get("type_id")
            db.session.commit()
            return redirect(url_for('moderators.moderators'))
