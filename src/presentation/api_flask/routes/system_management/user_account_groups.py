"""
    ToDo: DocString
"""

from mediatr import Mediator
from flask import Blueprint

user_account_groups = Blueprint("userAccountGroups", __name__)
mediator = Mediator()

@user_account_groups.route("/", methods=["POST"])
def create_user_account_group():
    """ ToDo: DocString """
    return "create_user_account_groups"


@user_account_groups.route("/<guid>", methods=["GET"])
def read_user_account_group(guid):
    """ ToDo: DocString """
    return f"read_user_account_groups {guid}"


@user_account_groups.route("/", methods=["GET"])
def search_user_account_groups():
    """ ToDo: DocString """
    return "search_user_account_groups"


@user_account_groups.route("/<guid>", methods=["PUT"])
def update_user_account_group(guid):
    """ ToDo: DocString """
    return f"update_user_account_groups {guid}"


@user_account_groups.route("/", methods=["DELETE"])
def delete_user_account_groups():
    """ ToDo: DocString """
    return "delete_user_account_groups"
