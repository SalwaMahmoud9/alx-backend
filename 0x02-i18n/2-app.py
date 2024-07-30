#!/usr/bin/env python3
'''Task 2
'''

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''Config'''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get_locale.

    Returns:
        str: request.accept_languages.best_match(app.config['LANGUAGES'])
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''index

    Returns:
        html: 2-index.html
    '''
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
