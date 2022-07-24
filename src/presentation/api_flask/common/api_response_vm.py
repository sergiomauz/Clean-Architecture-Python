# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=import-error

"""
    ToDo: DocString
"""

import json
from typing import Any
from .api_result_vm import ApiResultVm

class ApiResponseVm:
    def __init__(self, info: Any = None):
        self.info = info
        self.result = ApiResultVm()
        del self.info.__orig_class__

    @property
    def json_string(self):
        return json.dumps(self.__dict__, default = lambda obj: obj.__dict__)

    @property
    def json_object(self):
        return json.loads(self.json_string)
