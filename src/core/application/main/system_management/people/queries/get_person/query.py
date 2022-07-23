# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

import uuid

class GetPersonQuery:
    def __init__(self, uid: uuid) -> None:
        self.uid = uid
