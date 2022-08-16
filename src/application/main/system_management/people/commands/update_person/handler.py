"""
    ToDo: DocString
"""

from datetime import datetime
from mediatr import Mediator
from .command import UpdatePersonCommand
from .view_model import UpdatePersonVm

@Mediator.handler
class UpdatePersonHandler:
    """ ToDo: DocString """

    def handle(self, command: UpdatePersonCommand) -> UpdatePersonVm:
        """ ToDo: DocString """

        update_person_vm = UpdatePersonVm(
            command.uid, command.name, command.last_name, datetime.utcnow(), datetime.utcnow())

        return update_person_vm
