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


class BasicPersonVm:
    def __init__(self,
                 uid: uuid = None,
                 name: str = None,
                 last_name: str = None,
                 created_at: datetime = None,
                 modified_at: datetime = None) -> None:
        self.uid = uid
        self.name = name
        self.last_name = last_name
        self.created_at = created_at
        self.modified_at = modified_at
