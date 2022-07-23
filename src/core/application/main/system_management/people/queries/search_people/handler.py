# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from mediatr import Mediator
from .query import SearchPeopleQuery
from .view_model import SearchPeopleVm
from core.application.common.general import PagerVm


@Mediator.handler
class SearchPeopleHandler:
    def handle(self, query: SearchPeopleQuery) -> PagerVm[SearchPeopleVm]:
        people_list = []
        people_items = people_list
        total_items = 58

        search_people_vm = PagerVm(
            items = people_items,
            total_items = total_items,
            current_page = query.basic_search_parameters.current_page,
            page_size = query.basic_search_parameters.page_size
        )

        return search_people_vm
