"""
    ToDo: DocString
"""
from flask import Blueprint

people = Blueprint("people", __name__)
PATH_PEOPLE = "/people"

@people.route(PATH_PEOPLE, methods=["POST"])
def create_person():
    """ ToDo: DocString """
    return "create_person"


@people.route(f"{PATH_PEOPLE}/<guid>", methods=["GET"])
def read_person(guid):
    """ ToDo: DocString """
    return f"read_person {guid}"


@people.route(PATH_PEOPLE, methods=["GET"])
def search_people():
    """ ToDo: DocString """
    return "search_people"


@people.route(f"{PATH_PEOPLE}/<guid>", methods=["PUT"])
def update_person(guid):
    """ ToDo: DocString """
    return f"update_person {guid}"


@people.route(f"{PATH_PEOPLE}", methods=["DELETE"])
def delete_person():
    """ ToDo: DocString """
    return "delete_person"
