from flask import render_template, request, redirect, url_for
from . import auth_bp
from sample_project.utils import Alert_Success, Alert_Fail

@auth_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'user' and password == 'user_password':
            Alert_Success('Login successful!')
            return redirect(url_for('user.user_dashboard'))
        elif username == 'cashier' and password == 'cashier_password':
            Alert_Success('Login successful!')
            return redirect(url_for('cashier.cashier_dashboard'))
        else:
            Alert_Fail('Invalid credentials.')
    return render_template('login.html')
