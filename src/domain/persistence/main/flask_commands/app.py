"""
    ToDo: DocString
"""
import sys
from pathlib import Path
from flask import Flask
from flask_migrate import Migrate

ROOT_DIRECTORY = str(Path(__file__).parents[5])
sys.path.append(f"{ROOT_DIRECTORY}/src/")

from domain.persistence.main import set_connection, db_connector

app = Flask(__name__)
db = set_connection(app)
migrate = Migrate(app, db)


class User(db.Model):
    """ ToDo: DocString """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
