# pylint: disable=unused-import
# pylint: disable=import-error

"""
    ToDo: DocString
"""

from mediatr import Mediator
from flask import Blueprint, request
from startup import MediatorContainer
from core.application.main.system_management.people.commands.create_person import (
    CreatePersonCommand, CreatePersonVm, CreatePersonHandler)

people = Blueprint("people", __name__)
mediator = Mediator()

@people.route("/", methods=["POST"])
async def create_person():
    """ ToDo: DocString """
    command = CreatePersonCommand(request.json)
    view_model = await mediator.send_async(command)

    return view_model.json


@people.route("/<uid>", methods=["GET"])
def read_person(uid):
    """ ToDo: DocString """
    return f"read_person {uid}"


@people.route("/", methods=["GET"])
def search_people():
    """ ToDo: DocString """
    return "search_people"


@people.route("/<uid>", methods=["PUT"])
def update_person(uid):
    """ ToDo: DocString """
    return f"update_person {uid}"


@people.route("/", methods=["DELETE"])
def delete_person():
    """ ToDo: DocString """
    return "delete_person"
