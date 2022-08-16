"""
    ToDo: DocString
"""
from domain.persistence.main import db_connector as db
from .basic_entity import BasicEntity


class NamedEntity(BasicEntity):
    """ ToDo: DocString """
    name = db.Column(db.String(100), default = None)
