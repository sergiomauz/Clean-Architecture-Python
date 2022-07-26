# pylint: disable=unused-import
# pylint: disable=import-error

"""
    ToDo: DocString
"""

import uuid
from mediatr import Mediator
from flask import Blueprint, Response, request

from core.common.utils import Constants
from core.application.main.system_management.people.commands.create_person import (
    CreatePersonCommand, CreatePersonVm, CreatePersonHandler)
from core.application.main.system_management.people.queries.get_person import (
    GetPersonQuery, GetPersonVm, GetPersonHandler)
from core.application.main.system_management.people.queries.search_people import (
    SearchPeopleQuery, SearchPeopleVm, SearchPeopleHandler)
from core.application.main.system_management.people.commands.update_person import (
    UpdatePersonCommand, UpdatePersonVm, UpdatePersonHandler)
from core.application.main.system_management.people.commands.delete_person import (
    DeletePersonCommand, DeletePersonVm, DeletePersonHandler)

from presentation.api.common import ApiResponseVm


people = Blueprint("people", __name__)
mediator = Mediator()


@people.route("/", methods=["POST"])
async def create_person():
    """ ToDo: DocString """
    command = CreatePersonCommand.new(request)
    application_view_model = await mediator.send_async(command)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.status_code,
        mimetype = Constants.MIMETYPE_JSON
    )

@people.route("/", methods=["GET"])
async def search_people():
    """ ToDo: DocString """
    query = SearchPeopleQuery(request)
    application_view_model = await mediator.send_async(query)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.status_code,
        mimetype = Constants.MIMETYPE_JSON
    )

@people.route("/<uid>", methods=["GET"])
async def read_person(uid: uuid):
    """ ToDo: DocString """
    query = GetPersonQuery(uid)
    application_view_model = await mediator.send_async(query)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.status_code,
        mimetype = Constants.MIMETYPE_JSON
    )

@people.route("/", methods=["PUT"])
async def update_person():
    """ ToDo: DocString """
    command = UpdatePersonCommand(request)
    application_view_model = await mediator.send_async(command)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.status_code,
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
        status = api_response_view_model.result.status_code,
        mimetype = Constants.MIMETYPE_JSON
    )
