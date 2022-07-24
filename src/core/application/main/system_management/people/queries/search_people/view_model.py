# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name
# pylint: disable=import-error
# pylint: disable=too-many-arguments

"""
    ToDo: DocString
"""

import uuid
from datetime import datetime
from core.application.main.system_management.people.common import BasicPersonVm


class SearchPeopleVm(BasicPersonVm):
    def __init__(self,
                 uid: uuid = None,
                 name: str = None,
                 last_name: str = None,
                 created_at: datetime = None,
                 modified_at: datetime = None) -> None:
        self.uid = uid
        self.name = name
        self.last_name = last_name
        self.created_at = (created_at.isoformat() if created_at is not None else None)
        self.modified_at = (modified_at.isoformat() if modified_at is not None else None)
