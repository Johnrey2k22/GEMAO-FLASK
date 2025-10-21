from flask import render_template
from . import user_bp

@user_bp.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')
