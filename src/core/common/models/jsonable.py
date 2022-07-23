# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

"""
    ToDo: DocString
"""

import json

class Jsonable:
    @property
    def string(self):
        return json.dumps(self.__dict__, default = lambda obj: obj.__dict__)

    @property
    def json(self):
        return json.loads(self.string)
