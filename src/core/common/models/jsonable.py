# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

"""
    ToDo: DocString
"""

import json

class Jsonable:
    def __init__(self):
        pass

    @property
    def json(self):
        return json.loads(json.dumps(self.__dict__, default = lambda obj: obj.__dict__))
