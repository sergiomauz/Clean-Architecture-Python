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
    persistence_container = PersistenceContainer()
    persistence_container.wire(modules = [sys.modules[__name__]])

    print(type(__name__))

    app.run(debug = True)
