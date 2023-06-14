from flask import Blueprint, redirect, url_for, request, render_template
from decors.role_req import role_req

admin_bp = Blueprint('admin', __name__, template_folder='templates')


@admin_bp.route('/admin', methods=['GET', 'POST'])
@role_req(1)
def admin():
    return render_template("admin.html")