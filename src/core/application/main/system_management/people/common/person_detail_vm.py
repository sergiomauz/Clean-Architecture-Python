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
                 uid: uuid = None,
                 name: str = None,
                 last_name: str = None,
                 created_at: datetime = None,
                 modified_at: datetime = None) -> None:
        super().__init__(uid, name, last_name, created_at, modified_at)
