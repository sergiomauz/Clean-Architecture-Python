# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name
# pylint: disable=import-error
# pylint: disable=too-many-arguments

"""
    ToDo: DocString
"""

from datetime import datetime


class BasicPersonVm:
    def __init__(self,
                 uid: None,
                 name: str,
                 last_name: str,
                 created_at: datetime,
                 modified_at: datetime) -> None:
        self.uid = uid
        self.name = name
        self.last_name = last_name
        self.created_at = created_at
        self.modified_at = modified_at
