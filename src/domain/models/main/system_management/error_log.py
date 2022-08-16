"""
    ToDo: DocString
"""
from domain.main.basic_entity import BasicEntity
from domain.persistence import db_connector as db


class ErrorLog(BasicEntity):
    """ ToDo: DocString """
    status_code = db.Column(db.Integer, default = 0)
    description = db.Column(db.String(1500))
    stack_trace = db.Column(db.String(6150))
