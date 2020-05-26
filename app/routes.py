from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user

from app import App
from app.forms import LoginForm
from app.models import User


# из папки app импортирую экземпляр класса Flask по имени App


@App.route('/')
@App.route('/index')
def index():
    words = ['привет', 'пока', 'я очень буду ждать звонка', 'полетели', 'hello']
    '''
        я связываю МЕТКУ words на странице index.html
        со своим массивом words, в котором лежат слова
    '''
    return render_template('index.html', words=words)


@App.route('/sign_in', methods=['GET', 'POST'])
def signIn():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.checkPassword(form.password.data):
            flash('Неправильный логин и/или пароль')
            return redirect(url_for('signIn'))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('index'))

    return render_template('login.html', form=form)


@App.route('/sign_out')
def logout():
    logout_user()
    return redirect(url_for('index'))
