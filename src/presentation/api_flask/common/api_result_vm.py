# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=missing-class-docstring
# pylint: disable=import-error

"""
    ToDo: DocString
"""

class ApiResultVm:
    def __init__(self,
                 http_code: int = 200,
                 message: str = "",
                 style: str = ""):
        self.http_code = http_code
        self.message = message
        self.style = style
        