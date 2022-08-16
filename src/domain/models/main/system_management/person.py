"""
    ToDo: DocString
"""
from domain.main.named_entity import NamedEntity
from domain.persistence import db_connector as db


class Person(NamedEntity):
    """ ToDo: DocString """
    last_name = db.Column(db.String(100), default = None)
