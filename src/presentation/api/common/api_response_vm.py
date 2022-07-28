"""
    ToDo: DocString
"""

import json
from typing import Any

from core.application.main.system_management.error_log.commands.create_error_log import (
    CreateErrorLogVm)

from .api_result_vm import ApiResultVm
from .api_message_vm import ApiMessagesVm



class ApiResponseVm:
    """ ToDo: DocString """

    def __init__(self, info: Any = None):
        if hasattr(info, '__orig_class__'):
            del info.__orig_class__

        if not isinstance(info, CreateErrorLogVm):
            self.info = info
            self.result = ApiResultVm()
        else:
            self.info = self.__format_error_info(info)
            self.result = ApiResultVm(
                status_code = info.status_code,
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

    def __format_error_info(self, info: Any):
        """ ToDo: DocString """
        if info.status_code >= 500 and info.status_code < 600:
            return ApiMessagesVm(
                messages = [(0, "server_error",
                                "There was an unhandled error. Please contact the Administrator.")]
            )

        if info.status_code >= 400 and "(type=assertion_error)" in info.description:
            new_descriptions = info.description.replace("(type=assertion_error)","").split("\n")
            new_descriptions.pop(0)
            new_descriptions = [item.strip() for item in new_descriptions]

            errors_list = []
            for count, value in enumerate(new_descriptions):
                if count % 2 == 0:
                    errors_list.append((int(count / 2), value, new_descriptions[count + 1]))

            return ApiMessagesVm(
                messages = errors_list
            )

        return ApiMessagesVm(
            messages = info.description
        )
