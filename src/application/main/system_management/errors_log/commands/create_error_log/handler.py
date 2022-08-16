"""
    ToDo: DocString
"""

from datetime import datetime
from mediatr import Mediator
from .command import CreateErrorLogCommand
from .view_model import CreateErrorLogVm

@Mediator.handler
class CreateErrorLogHandler:
    """ ToDo: DocString """

    def handle(self, command: CreateErrorLogCommand) -> CreateErrorLogVm:
        """ ToDo: DocString """

        create_error_log_vm = CreateErrorLogVm(
            command.status_code, command.description,
            command.stack_trace, datetime.utcnow()
        )
        return create_error_log_vm
