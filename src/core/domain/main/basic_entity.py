# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

"""
    ToDo: DocString
"""

from datetime import datetime

class BasicEntity:
    def __init__(self):
        self.id = None
        self.created_at = datetime.utcnow()
        self.modified_at = None

    @property
    def id(self):
        return self.id

    @property
    def created_at(self):
        return self.created_at

    @property
    def modified_at(self):
        return self.modified_at

    @id.setter
    def id(self, new_value):
        self.id = new_value

    @created_at.setter
    def create_at(self, new_value):
        self.created_at = new_value

    @modified_at.setter
    def modified_at(self, new_value):
        self.modified_at = new_value
