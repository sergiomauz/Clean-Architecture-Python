"""
    ToDo: DocString
"""


from flask import Flask
from presentation.routes_handler import RoutesHandler
from presentation.custom_exceptions_handler import CustomExceptionsHandler


app = Flask(__name__)
routes_handler = RoutesHandler()
routes_handler.start_routes(app)
exceptions_handler = CustomExceptionsHandler()
exceptions_handler.start_custom_exceptions(app)

if __name__ == "__main__":
    app.run(debug = True)
