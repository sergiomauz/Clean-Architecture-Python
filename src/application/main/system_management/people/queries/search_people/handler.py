"""
    ToDo: DocString
"""

from mediatr import Mediator
from application.common.general import PagerVm
from .query import SearchPeopleQuery
from .view_model import SearchPeopleVm


@Mediator.handler
class SearchPeopleHandler:
    """ ToDo: DocString """

    def handle(self, query: SearchPeopleQuery) -> PagerVm[SearchPeopleVm]:
        """ ToDo: DocString """

        people_list = []
        people_items = people_list
        total_items = 58

        search_people_vm = PagerVm[SearchPeopleVm](
            items = people_items,
            total_items = total_items,
            current_page = query.basic_search_parameters.current_page,
            page_size = query.basic_search_parameters.page_size
        )

        return search_people_vm
