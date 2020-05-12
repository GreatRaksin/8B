from flask import render_template
from app import App

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
