"""
    ToDo: DocString
"""

import sys
from flask import Flask
from infrastructure.persistence.persistence_container import PersistenceContainer
from presentation.api_flask.routes.start_routes import start_routes

app = Flask(__name__)

# Start routes
start_routes(app)

if __name__ == '__main__':
    app.run(debug = True)
