"""
    ToDo: DocString
"""

from mediatr import Mediator
from .command import DeletePersonCommand
from .view_model import DeletePersonVm

@Mediator.handler
class DeletePersonHandler:
    """ ToDo: DocString """

    def handle(self, command: DeletePersonCommand) -> DeletePersonVm:
        """ ToDo: DocString """

        delete_person_vm = DeletePersonVm(True)

        return delete_person_vm
