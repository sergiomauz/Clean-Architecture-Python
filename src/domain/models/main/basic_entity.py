"""
    ToDo: DocString
"""
import uuid
from sqlalchemy.dialects.postgresql import UUID as psqlUUID
from domain.persistence.main import db_connector as db


class BasicEntity(db.Model):
    """ ToDo: DocString """
    uid = db.Column(psqlUUID(as_uuid = True), primary_key = True, default = uuid.UUID(int = 0))
    created_at = db.Column(db.DateTime, nullable = False)
    modified_at = db.Column(db.DateTime, nullable = True)
