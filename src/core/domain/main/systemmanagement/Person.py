# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

"""
    ToDo: DocString
"""

from NamedEntity import NamedEntity

class Person(NamedEntity):
    def __init__(self):
        super().__init__()
        self.last_name = None

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, new_value):
        self.last_name = new_value
    