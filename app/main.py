from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Chat
from . import db

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    chat = Chat.query.order_by(Chat.id).all()
    return render_template('index.html', chat=chat)


@main.route('/', methods=['POST'])
@login_required
def send():
    message = request.form.get('chat-input')
    username = current_user.username

    new_message = Chat(message=message, username=username)

    db.session.add(new_message)
    db.session.commit()

    return redirect(url_for('main.index'))
