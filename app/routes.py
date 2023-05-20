from app import app, db
from app.models import User, Post
from werkzeug.urls import url_parse
from app.forms import LoginForm, SignupForm, ChatForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, logout_user, login_user, current_user


@app.route('/', methods=['POST', 'GET'])
@login_required
def index():
    form = ChatForm()
    if form.validate_on_submit():
        post = Post(message=form.chat.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    chat = Post.query.order_by(Post.id).all()
    return render_template('index.html', title='Global', chat=chat, form=form)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Incorrect login data, try again')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
