# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name
# pylint: disable=import-error
# pylint: disable=too-many-arguments

"""
    ToDo: DocString
"""

from core.application.main.system_management.people.queries.get_person.view_model import GetPersonVm


class SearchPeopleVm:
    def __init__(self, get_person_vm: GetPersonVm = None) -> None:
        self.get_person_vm = get_person_vm
