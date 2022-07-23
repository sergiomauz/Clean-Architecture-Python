# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from mediatr import Mediator
from .command import DeletePersonCommand
from .view_model import DeletePersonVm

@Mediator.handler
class DeletePersonHandler:
    def handle(self, command: DeletePersonCommand) -> DeletePersonVm:
        delete_person_vm = DeletePersonVm(True)

        return delete_person_vm
