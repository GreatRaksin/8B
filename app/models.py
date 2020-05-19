from app import db


class User(db.Model):
    """ описываю таблицу, в которой будут храниться данные пользователей """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))