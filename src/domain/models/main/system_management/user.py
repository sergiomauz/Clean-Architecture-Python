"""
    ToDo: DocString
"""
from domain.persistence.main import db_connector as db


class User(db.Model):
    """ ToDo: DocString """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
