from flask import Blueprint, redirect, url_for, request, render_template

admin_bp = Blueprint('admin', __name__, template_folder='templates')


@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template("admin.html")