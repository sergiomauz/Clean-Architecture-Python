"""
    ToDo: DocString
"""
from flask import Flask
from flask_migrate import Migrate
from domain.persistence.main import set_connection, db_connector
from api.routes import RoutesHandler
from api.exceptions import CustomExceptionsHandler


app = Flask(__name__)
db = set_connection(app)


migrate = Migrate(app, db)

routes_handler = RoutesHandler()
routes_handler.start_routes(app)

exceptions_handler = CustomExceptionsHandler()
exceptions_handler.start_custom_exceptions(app)


# print("============================")
# print(x)
# print("============================")
# print(db_connector)
# print("============================")

# class User(db.Model):
#     """ ToDo: DocString """
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))


if __name__ == "__main__":
    app.run(debug = True)
