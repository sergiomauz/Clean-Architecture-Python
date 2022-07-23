# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from datetime import datetime
from mediatr import Mediator
from .command import UpdatePersonCommand
from .view_model import UpdatePersonVm

@Mediator.handler
class UpdatePersonHandler:
    def handle(self, command: UpdatePersonCommand) -> UpdatePersonVm:
        update_person_vm = UpdatePersonVm(
            command.uid, command.name, command.last_name, datetime.utcnow(), datetime.utcnow())

        return update_person_vm
