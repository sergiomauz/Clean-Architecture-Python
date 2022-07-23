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
from .basic_person_vm import BasicPersonVm


class PersonDetailVm(BasicPersonVm):
    def __init__(self,
                 uid: uuid,
                 name: str,
                 last_name: str,
                 created_at: datetime,
                 modified_at: datetime) -> None:
        super().__init__(self, uid, name, last_name, created_at, modified_at)
