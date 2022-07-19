# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from .dto import CreatePersonCommandDto

class CreatePersonCommand:
    def __init__(self, dto: CreatePersonCommandDto):
        self.name = dto.name
        self.last_name = dto.last_name
