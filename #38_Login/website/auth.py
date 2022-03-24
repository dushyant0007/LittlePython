from curses.ascii import NUL
import email
from hashlib import sha256
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from website import db, views
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        email_ = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email_).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user,remember=True)
                return redirect(url_for(views.home))
            else:
                flash('Incorrect Password, try again')
        else:
            flash('User Not Found')

    return render_template("login.html", boolean=True)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist')
        else:
            name = request.form.get('name')
            email_ = request.form.get("email")
            password = request.form.get('password')
            new_user = User(name=name, email=email_, password=generate_password_hash(password, method=sha256))
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember=True)
            flash(" Account Created! ", category="success")
            return redirect(url_for(views.home))

    return render_template("sign_up.html")
