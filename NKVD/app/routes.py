from functools import wraps
from datetime import datetime, timedelta

import jwt
from flask import Flask
from flask import jsonify
from flask import request, redirect, url_for, flash, render_template, make_response
from flask_login import current_user, login_required, logout_user, login_user
from flask_jwt_extended import get_jwt, get_jwt_header
from werkzeug.urls import url_parse
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from app import app, db
from app.forms import LoginForm, RegistrationForm, FlagForm
from app.models import User, Flag


def set_cookie(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        response = f(*args, **kws)
        response = make_response(response)
        if request.cookies.get('access_token') is None:
            response.set_cookie('access_token', value=current_user.create_token(),
                                expires=datetime.now() + timedelta(days=30))
        return response
    return decorated_function


@app.route('/')
@app.route('/index')
@login_required
@set_cookie
def index():
    form = FlagForm()
    return render_template('index.html', title='Home', form=form, flags=current_user.flags.all())


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        user.flag = form.flag.data
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html',  title='Sign In', form=form)


@app.route('/profile', methods=['GET'])
@login_required
def user():
    token = request.cookies.get('access_token')
    return render_template('profile.html', title='Profile', token=token)


@app.route('/logout')
def logout():
    logout_user()
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('access_token')
    return response


@app.route("/public_key", methods=['GET'])
def get_public_key():
    return app.config['JWT_PUBLIC_KEY']
