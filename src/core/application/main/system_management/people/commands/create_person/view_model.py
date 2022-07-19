# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name
# pylint: disable=import-error

"""
    ToDo: DocString
"""

from core.common.models.jsonable import Jsonable

class CreatePersonVm(Jsonable):
    def __init__(self, uid, name, last_name, created_at, modified_at):
        super().__init__()
        self.uid = uid
        self.name = name
        self.last_name = last_name
        self.created_at = (created_at.isoformat() if created_at is not None else None)
        self.modified_at = (modified_at.isoformat() if modified_at is not None else None)
