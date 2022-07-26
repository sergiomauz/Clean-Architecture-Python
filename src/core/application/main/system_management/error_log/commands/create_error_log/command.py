# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

import traceback
from typing import Any
from pydantic import ValidationError

class CreateErrorLogCommand:
    def __init__(self, exception: Any = None):
        self.description = str(exception)
        self.stack_trace = "".join(traceback.format_tb(exception.__traceback__))

        if isinstance(exception, ValidationError):
            self.status_code = 400
        else:
            self.status_code = 500
