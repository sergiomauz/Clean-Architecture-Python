"""
    ToDo: DocString
"""
from domain.models.main import BasicEntity
from domain.persistence.main import sql_alchemy as db


class ErrorLog(BasicEntity):
    """ ToDo: DocString """
    status_code = db.Column(db.Integer, default = 0)
    description = db.Column(db.String(1500))
    stack_trace = db.Column(db.String(6150))
