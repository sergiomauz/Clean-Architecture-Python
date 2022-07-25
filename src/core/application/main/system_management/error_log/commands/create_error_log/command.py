# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

import traceback
from typing import Any


class CreateErrorLogCommand:
    def __init__(self, exception: Any = None):
        self.description = str(exception)
        self.stack_trace = "".join(traceback.format_tb(exception.__traceback__))

        if isinstance(exception, Exception):
            self.status_code = 500
        else:
            self.status_code = 401
