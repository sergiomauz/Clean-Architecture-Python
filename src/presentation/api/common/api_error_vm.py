# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=import-error

"""
    ToDo: DocString
"""

class ApiErrorVm(Exception):
    def __init__(self, message : str = "", status_code : int = 400):
        super().__init__()
        self.message = message
        self.status_code = status_code
