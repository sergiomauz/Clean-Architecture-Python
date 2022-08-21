"""
    ToDo: DocString
"""
import sys
from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

ROOT_DIRECTORY = str(Path(__file__).parents[3])
sys.path.append(f"{ROOT_DIRECTORY}")

from settings import AppSettings

sql_alchemy = SQLAlchemy()

def set_connection(app: Flask) -> SQLAlchemy:
    """ ToDo: DocString """
    settings = AppSettings()
    host = settings.get("POSTGRESQL.HOST")
    port = settings.get("POSTGRESQL.PORT")
    user = settings.get("POSTGRESQL.USER")
    password = settings.get("POSTGRESQL.PASSWORD")
    database = settings.get("POSTGRESQL.DATABASE")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    sql_alchemy.app = app
    sql_alchemy.init_app(app)

    return sql_alchemy
