"""
    ToDo: DocString
"""
from flask import Flask
from domain.persistence.main import set_connection
from api.routes import RoutesHandler
from api.exceptions import CustomExceptionsHandler


app = Flask(__name__)

routes_handler = RoutesHandler()
routes_handler.start_routes(app)

set_connection(app)

exceptions_handler = CustomExceptionsHandler()
exceptions_handler.start_custom_exceptions(app)

if __name__ == "__main__":
    app.run(debug = True)
