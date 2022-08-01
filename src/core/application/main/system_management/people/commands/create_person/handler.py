"""
    ToDo: DocString
"""

from datetime import datetime
from mediatr import Mediator
from .command import CreatePersonCommand
from .view_model import CreatePersonVm

@Mediator.handler
class CreatePersonHandler:
    """ ToDo: DocString """

    def handle(self, command: CreatePersonCommand) -> CreatePersonVm:
        """ ToDo: DocString """

        create_person_vm = CreatePersonVm(
            None, command.name, command.last_name, datetime.utcnow(), None)

        return create_person_vm
