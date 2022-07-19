# pylint: disable=unused-import
# pylint: disable=import-error
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from mediatr import Mediator
from flask import Blueprint, request
from core.application.main.systemmanagement.people.commands.createperson import (
    CreatePersonCommand, CreatePersonVm, CreatePersonHandler)

people = Blueprint("people", __name__)
mediator = Mediator()

@people.route("/", methods=["POST"])
async def create_person():
    """ ToDo: DocString """
    command = CreatePersonCommand(request)
    view_model = await mediator.send_async(command)

    return view_model.json


@people.route("/<guid>", methods=["GET"])
def read_person(guid):
    """ ToDo: DocString """
    return f"read_person {guid}"


@people.route("/", methods=["GET"])
def search_people():
    """ ToDo: DocString """
    return "search_people"


@people.route("/<guid>", methods=["PUT"])
def update_person(guid):
    """ ToDo: DocString """
    return f"update_person {guid}"


@people.route("/", methods=["DELETE"])
def delete_person():
    """ ToDo: DocString """
    return "delete_person"
