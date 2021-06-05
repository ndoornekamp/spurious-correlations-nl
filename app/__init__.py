from flask import Flask, request, session
from flask_babel import Babel

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'any random string'
babel = Babel(app)


# Load the views
from app import views

# Load the config file
app.config.from_object('config')


@babel.localeselector
def get_locale():
    session_locale = session.get('locale', None)
    if session_locale:
        return session_locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
