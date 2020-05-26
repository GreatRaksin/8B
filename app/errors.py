from flask import render_template
from app import App, db

@App.errorhandler(404)
def notFound(error):
    return render_template('404.html'), 404

@App.errorhandler(500)
def badGateway(error):
    db.session.rollback()
    return render_template('500.html'), 500