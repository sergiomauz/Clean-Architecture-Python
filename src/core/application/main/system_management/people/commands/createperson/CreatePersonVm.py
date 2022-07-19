# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

"""
    ToDo: DocString
"""

import json

class CreatePersonVm:
    def __init__(self):
        self.id = None
        self.name = None
        self.last_name = None
        self.created_at = None
        self.modified_at = None

    @property
    def json(self):
        return json.loads(json.dumps(self.__dict__, default = lambda obj: obj.__dict__))
