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

from core.application.main.system_management.error_log.commands.create_error_log import (
    CreateErrorLogVm)

from .api_result_vm import ApiResultVm
from .api_message_vm import ApiMessageVm



class ApiResponseVm:
    def __init__(self, info: Any = None):
        if hasattr(info, '__orig_class__'):
            del info.__orig_class__

        if not isinstance(info, CreateErrorLogVm):
            self.info = info
            self.result = ApiResultVm()
        else:
            if info.status_code >= 500 and info.status_code < 600:
                self.info = ApiMessageVm(
                    message = "There was an unhandled error. Please contact the Administrator"
                )
            else:
                self.info = ApiMessageVm(
                    message = info.description
                )
            self.result = ApiResultVm(
                status_code = info.status_code,
                is_exception = True,
                style = ""
            )

    @property
    def json_string(self):
        return json.dumps(self.__dict__, default = lambda obj: obj.__dict__)

    @property
    def json_object(self):
        return json.loads(self.json_string)
