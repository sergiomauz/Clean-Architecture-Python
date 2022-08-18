"""
    ToDo: DocString
"""
from domain.models.main import NamedEntity
from domain.persistence.main import db_connector as db


class Person(NamedEntity):
    """ ToDo: DocString """
    last_name = db.Column(db.String(100), default = None)
