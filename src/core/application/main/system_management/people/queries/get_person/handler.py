# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from datetime import datetime
from mediatr import Mediator
from .query import GetPersonQuery
from .view_model import GetPersonVm

@Mediator.handler
class GetPersonHandler:
    def handle(self, query: GetPersonQuery) -> GetPersonVm:
        get_person_vm = GetPersonVm(
            "cb4c3fb3-5580-42aa-ab3f-a63941374e4f",
            "Sergio Mauricio",
            "Zambrano Jove",
            datetime.utcnow(),
            datetime.utcnow())

        return get_person_vm
