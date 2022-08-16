"""
    ToDo: DocString
"""

import uuid
from datetime import datetime


class CreatePersonVm:
    """ ToDo: DocString """

    def __init__(self,
                 uid: uuid = None,
                 name: str = None,
                 last_name: str = None,
                 created_at: datetime = None,
                 modified_at: datetime = None):
        """ ToDo: DocString """

        self.uid = uid
        self.name = name
        self.last_name = last_name
        self.created_at = (created_at.isoformat() if created_at is not None else None)
        self.modified_at = (modified_at.isoformat() if modified_at is not None else None)
