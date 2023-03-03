#!/usr/bin/env python3
"""
Basic Flask app
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Babel configuration
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route("/")
def index():
    """
    renders index html page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)