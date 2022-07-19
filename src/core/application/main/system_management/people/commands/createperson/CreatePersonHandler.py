"""
    ToDo: DocString
"""
from mediatr import Mediator

from .CreatePersonCommand import CreatePersonCommand
from .CreatePersonVm import CreatePersonVm

@Mediator.handler
class CreatePersonHandler():
    """ ToDo: DocString """
    def handle(self, request: CreatePersonCommand) -> CreatePersonVm:
        """ ToDo: DocString """
        create_person_vm = CreatePersonVm()
        create_person_vm.name = request.name
        create_person_vm.last_name = request.last_name

        return create_person_vm
