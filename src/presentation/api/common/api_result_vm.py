# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=missing-class-docstring
# pylint: disable=import-error

"""
    ToDo: DocString
"""

class ApiResultVm:
    def __init__(self,
                 status_code: int = 200,
                 is_exception: bool = False,
                 style: str = ""):
        self.status_code = status_code
        self.is_exception = is_exception
        self.style = style
        