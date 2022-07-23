# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from typing import Any


class CreatePersonCommand:
    def __init__(self, request: Any):
        self.name = request.json["name"]
        self.last_name = request.json["last_name"]
