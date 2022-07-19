# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

"""
    ToDo: DocString
"""

from basic_entity import BasicEntity

class NamedEntity(BasicEntity):
    def __init__(self):
        super().__init__()
        self.name = None

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_value):
        self.name = new_value
