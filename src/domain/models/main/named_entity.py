"""
    ToDo: DocString
"""
from domain.persistence.main import sql_alchemy as db
from .basic_entity import BasicEntity


class NamedEntity(BasicEntity):
    """ ToDo: DocString """
    __abstract__ = True
    name = db.Column(db.String(100), default = None)
