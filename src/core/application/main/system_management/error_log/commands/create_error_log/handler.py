# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from datetime import datetime
from mediatr import Mediator
from .command import CreateErrorLogCommand
from .view_model import CreateErrorLogVm

@Mediator.handler
class CreateErrorLogHandler:
    def handle(self, command: CreateErrorLogCommand) -> CreateErrorLogVm:
        create_error_log_vm = CreateErrorLogVm(
            command.status_code, command.description,
            command.stack_trace, datetime.utcnow()
        )
        return create_error_log_vm
