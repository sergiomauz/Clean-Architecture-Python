"""
    ToDo: DocString
"""
from flask import Blueprint

user_account_groups = Blueprint("userAccountGroups", __name__)
PATH_USER_ACCOUNT_GROUPS = "/userAccountGroups"

@user_account_groups.route(PATH_USER_ACCOUNT_GROUPS, methods=["POST"])
def create_user_account_group():
    """ ToDo: DocString """
    return "create_user_account_groups"


@user_account_groups.route(f"{PATH_USER_ACCOUNT_GROUPS}/<guid>", methods=["GET"])
def read_user_account_group(guid):
    """ ToDo: DocString """
    return f"read_user_account_groups {guid}"


@user_account_groups.route(PATH_USER_ACCOUNT_GROUPS, methods=["GET"])
def search_user_account_groups():
    """ ToDo: DocString """
    return "search_user_account_groups"


@user_account_groups.route(f"{PATH_USER_ACCOUNT_GROUPS}/<guid>", methods=["PUT"])
def update_user_account_group(guid):
    """ ToDo: DocString """
    return f"update_user_account_groups {guid}"


@user_account_groups.route(f"{PATH_USER_ACCOUNT_GROUPS}", methods=["DELETE"])
def delete_user_account_group():
    """ ToDo: DocString """
    return "delete_user_account_groups"
