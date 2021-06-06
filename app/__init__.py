import os

from flask import Flask, request, session
from flask_babel import Babel

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# This causes the secret key to change with every reboot, but that's no problem for this application: the only thing
# the secret key is used for is the session, which in its turn is only used to store the locale if the user wants to
# change that with respect to their browser's default
app.secret_key = os.urandom(24)
babel = Babel(app)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')


@babel.localeselector
def get_locale():
    session_language = session.get('language', None)
    if session_language:
        return session_language
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
