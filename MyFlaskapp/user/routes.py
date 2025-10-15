from flask import render_template
from . import user_bp
from MyFlaskapp.authentication.decorators import login_required

@user_bp.route('/user_dashboard')
@login_required
def user_dashboard():
    return render_template('user_dashboard.html')
