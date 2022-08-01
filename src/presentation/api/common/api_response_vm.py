"""
    ToDo: DocString
"""

import json
from typing import Any

from core.application.main.system_management.errors_log.commands.create_error_log import (
    CreateErrorLogVm)

from .api_result_vm import ApiResultVm
from .api_message_vm import ApiMessagesVm


class ApiResponseVm:
    """ ToDo: DocString """
    info: Any
    result: Any

    def __init__(self, info: Any = None):
        self.info = self.__set_info(info)
        self.result = self.__set_result(info)

    def __set_info(self, info_value: Any):
        """ ToDo: DocString """
        if hasattr(info_value, '__orig_class__'):
            del info_value.__orig_class__

        if not isinstance(info_value, CreateErrorLogVm):
            return info_value

        if info_value.status_code >= 500 and info_value.status_code < 600:
            return ApiMessagesVm(
                messages = [(0, "server_error",
                                "There was an unhandled error. Please contact the Administrator.")]
            )

        if info_value.status_code >= 400 and "(type=assertion_error)" in info_value.description:
            new_descriptions = info_value.description.replace("(type=assertion_error)",
                                                            "").split("\n")
            new_descriptions.pop(0)
            new_descriptions = [item.strip() for item in new_descriptions]

            errors_list = []
            for count, info_value in enumerate(new_descriptions):
                if count % 2 == 0:
                    errors_list.append((int(count / 2), info_value, new_descriptions[count + 1]))

            return ApiMessagesVm(
                messages = errors_list
            )

        return ApiMessagesVm(
            messages = info_value.description
        )

    def __set_result(self, info_value: Any):
        """ ToDo: DocString """
        if not isinstance(info_value, CreateErrorLogVm):
            return ApiResultVm()

        return ApiResultVm(
            status_code = info_value.status_code,
            is_exception = True,
            style = ""
        )

    @property
    def json_string(self):
        """ ToDo: DocString """
        return json.dumps(self.__dict__, default = lambda obj: obj.__dict__)

    @property
    def json_object(self):
        """ ToDo: DocString """
        return json.loads(self.json_string)
