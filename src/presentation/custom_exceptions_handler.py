"""
    ToDo: DocString
"""


from typing import Any
from mediatr import Mediator
from flask import Response

from core.common.utils import Constants
from core.application.main.system_management.errors_log.commands.create_error_log import (
    CreateErrorLogCommand, CreateErrorLogVm, CreateErrorLogHandler)

from .api.common import ApiResponseVm


class CustomExceptionsHandler:
    """ ToDo: DocString """
    mediator = Mediator()

    def start_custom_exceptions(self, app):
        """ ToDo: DocString """
        app.register_error_handler(Exception, self.api_error_response)

    def api_error_response(self, exception : Any):
        """ ToDo: DocString """
        command = CreateErrorLogCommand(exception)
        error_view_model = self.mediator.send(command)
        api_response_view_model = ApiResponseVm(error_view_model)

        return Response(
            response = api_response_view_model.json_string,
            status = api_response_view_model.result.status_code,
            mimetype = Constants.MIMETYPE_JSON
        )
