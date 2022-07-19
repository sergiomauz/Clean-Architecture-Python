# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from datetime import datetime
from mediatr import Mediator
from .command import CreatePersonCommand
from .view_model import CreatePersonVm

@Mediator.handler
class CreatePersonHandler:
    def handle(self, command: CreatePersonCommand) -> CreatePersonVm:
        create_person_vm = CreatePersonVm(
            None, command.name, command.last_name, datetime.utcnow(), datetime.utcnow())

        return create_person_vm
