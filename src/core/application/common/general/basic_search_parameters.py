# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from typing import Any

class BasicSearchParameters:
    def __init__(self, request: Any = None) -> None:
        self.current_page = request.args.get(key = "current_page", default = 1, type = int)
        self.page_size = request.args.get(key = "page_size", default = 25, type = int)
        self.filter_value = request.args.get(key = "filter_value", default = "", type = str)
