# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

import math
from typing import Generic, List, TypeVar

T = TypeVar("T")

class PagerVm(Generic[T]):
    def __init__(self,
                 items: List[T] = None,
                 total_items: int = 0,
                 current_page: int = 1,
                 page_size: int = 10) -> None:
        self.total_items = total_items
        self.current_page = current_page

        if page_size > 0:
            self.page_size = page_size
            self.total_pages = math.ceil(self.total_items / self.page_size)
            if self.total_pages == 0:
                self.total_pages = 1
        else:
            self.page_size = total_items
            self.total_pages = 1

        self.first_item = self.page_size * (self.current_page - 1) + 1
        if self.total_items > self.page_size * self.current_page:
            self.last_item = self.page_size * self.current_page
        else:
            self.last_item = self.total_items
        if items is not None:
            self.items = items
        else:
            self.items = []

    # @property
    # def items(self):
    #     return self.items

    # @items.setter
    # def items(self, new_value):
    #     self.items = new_value

    # @property
    # def total_items(self):
    #     return self.total_items

    # @total_items.setter
    # def total_items(self, new_value):
    #     self.total_items = new_value

    # @property
    # def current_page(self):
    #     return self.current_page

    # @current_page.setter
    # def current_page(self, new_value):
    #     self.current_page = new_value

    # @property
    # def page_size(self):
    #     return self.page_size

    # @page_size.setter
    # def page_size(self, new_value):
    #     self.page_size = new_value

    # @property
    # def total_pages(self):
    #     return self.total_pages

    # @total_pages.setter
    # def total_pages(self, new_value):
    #     self.total_pages = new_value
