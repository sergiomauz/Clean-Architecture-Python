"""
    ToDo: DocString
"""

import traceback
from typing import Any
from pydantic import ValidationError

class CreateErrorLogCommand:
    """ ToDo: DocString """

    def __init__(self, exception: Any = None):
        """ ToDo: DocString """

        self.description = str(exception)
        self.stack_trace = "".join(traceback.format_tb(exception.__traceback__))

        if isinstance(exception, ValidationError):
            self.status_code = 400
        else:
            self.status_code = 500
