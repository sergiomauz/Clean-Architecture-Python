# pylint: disable=unused-import
# pylint: disable=import-error

"""
    ToDo: DocString
"""

from flask import Blueprint, Response, request
from mediatr import Mediator
from presentation.api_flask.common import ApiResponseVm, Constants

from core.application.main.system_management.people.commands.create_person import (
    CreatePersonCommand, CreatePersonVm, CreatePersonHandler)

from core.application.main.system_management.people.commands.update_person import (
    UpdatePersonCommand, UpdatePersonVm, UpdatePersonHandler)
from core.application.main.system_management.people.commands.delete_person import (
    DeletePersonCommand, DeletePersonVm, DeletePersonHandler)


people = Blueprint("people", __name__)
mediator = Mediator()


@people.route("/", methods=["POST"])
async def create_person():
    """ ToDo: DocString """
    command = CreatePersonCommand(request)
    application_view_model = await mediator.send_async(command)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.http_code,
        mimetype = Constants.MIMETYPE_JSON
    )


@people.route("/<uid>", methods=["GET"])
def read_person(uid):
    """ ToDo: DocString """
    return f"read_person {uid}"


@people.route("/", methods=["GET"])
def search_people():
    """ ToDo: DocString """
    return "search_people"


@people.route("/", methods=["PUT"])
async def update_person():
    """ ToDo: DocString """
    command = UpdatePersonCommand(request)
    application_view_model = await mediator.send_async(command)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.http_code,
        mimetype = Constants.MIMETYPE_JSON
    )


@people.route("/", methods=["DELETE"])
async def delete_person():
    """ ToDo: DocString """
    command = DeletePersonCommand(request)
    application_view_model = await mediator.send_async(command)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.http_code,
        mimetype = Constants.MIMETYPE_JSON
    )
