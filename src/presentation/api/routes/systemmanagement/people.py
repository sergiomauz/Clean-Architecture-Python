"""
    ToDo: DocString
"""
from flask import Blueprint, jsonify, json
from mediatr import Mediator

from core.application.main.systemmanagement.people.commands.createperson.CreatePersonCommand import CreatePersonCommand

people = Blueprint("people", __name__)
mediator = Mediator()

@people.route("/", methods=["POST"])
def create_person():
    """ ToDo: DocString """
    return "create_person"


@people.route("/<guid>", methods=["GET"])
def read_person(guid):
    """ ToDo: DocString """
    return f"read_person {guid}"


@people.route("/", methods=["GET"])
def search_people():
    """ ToDo: DocString """
    request = CreatePersonCommand()
    request.name = "Sergio"
    request.last_name = "Zambrano"
    # result = mediator.send(request)

    return json.dumps(request)


@people.route("/<guid>", methods=["PUT"])
def update_person(guid):
    """ ToDo: DocString """
    return f"update_person {guid}"


@people.route("/", methods=["DELETE"])
def delete_person():
    """ ToDo: DocString """
    return "delete_person"
