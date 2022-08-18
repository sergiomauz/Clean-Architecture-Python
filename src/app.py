"""
    ToDo: DocString
"""
from flask import Flask
from flask_migrate import Migrate
from domain.persistence.main import set_connection
from api.routes import RoutesHandler
from api.exceptions import CustomExceptionsHandler


app = Flask(__name__)

db_connector = set_connection(app)
migrate = Migrate(app, db_connector)

routes_handler = RoutesHandler()
routes_handler.start_routes(app)

exceptions_handler = CustomExceptionsHandler()
exceptions_handler.start_custom_exceptions(app)



class User(db_connector.Model):
    id = db_connector.Column(db_connector.Integer, primary_key=True)
    name = db_connector.Column(db_connector.String(128))






if __name__ == "__main__":
    app.run(debug = True)
