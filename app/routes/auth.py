# routes/auth.py
from flask import Blueprint, render_template, request, redirect
from app.model import User, db
from flask_login import login_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()

        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect('/dashboard')

    return render_template('login.html')