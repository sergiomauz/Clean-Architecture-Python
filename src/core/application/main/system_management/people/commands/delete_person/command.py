# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=missing-class-docstring
# pylint: disable=import-error

"""
    ToDo: DocString
"""
from typing import Any


class DeletePersonCommand:
    def __init__(self, request: Any):
        self.uids = request.json["uids"]
