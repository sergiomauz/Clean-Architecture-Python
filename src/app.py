"""
    ToDo: DocString
"""

from flask import Flask
from presentation.routes_handler import start_routes
from presentation.exceptions_handler import start_exceptions_handler

app = Flask(__name__)


start_exceptions_handler(app)
start_routes(app)


if __name__ == '__main__':
    app.run(debug = True)
