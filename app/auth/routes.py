from flask import render_template, request, redirect, url_for, flash
from . import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'user' and password == 'user_password':
            return redirect(url_for('user.user_dashboard'))
        elif username == 'cashier' and password == 'cashier_password':
            return redirect(url_for('cashier.cashier_dashboard'))
        else:
            flash('Incorrect credentials')
    return render_template('login.html')
