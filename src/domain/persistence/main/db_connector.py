"""
    ToDo: DocString
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import AppSettings


db_connector = SQLAlchemy()

def set_connection(app: Flask):
    """ ToDo: DocString """
    settings = AppSettings()
    host = settings.get("POSTGRESQL.HOST")
    # port = settings.get("POSTGRESQL.PORT")
    user = settings.get("POSTGRESQL.USER")
    password = settings.get("POSTGRESQL.PASSWORD")
    database = settings.get("POSTGRESQL.DATABASE")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{password}@{host}/{database}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db_connector.app = app
    migrate = Migrate(app, db_connector)
