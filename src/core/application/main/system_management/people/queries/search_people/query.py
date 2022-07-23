# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from typing import Any

from core.application.common.general import BasicSearchParameters


class SearchPeopleQuery:
    def __init__(self, request: Any) -> None:
        self.basic_search_parameters = BasicSearchParameters(request)
