"""
    ToDo: DocString
"""

from flask import Blueprint

user_accounts = Blueprint("userAccounts", __name__)

@user_accounts.route("/", methods=["POST"])
def create_user_account():
    """ ToDo: DocString """
    return "create_user_account"


@user_accounts.route("/<guid>", methods=["GET"])
def read_user_account(guid):
    """ ToDo: DocString """
    return f"read_user_account {guid}"


@user_accounts.route("/", methods=["GET"])
def search_user_accounts(search):
    """ ToDo: DocString """
    return f"search_user_accounts {search}"


@user_accounts.route("/<guid>", methods=["PUT"])
def update_user_account(guid):
    """ ToDo: DocString """
    return f"update_user_account {guid}"


@user_accounts.route("/", methods=["DELETE"])
def delete_user_accounts():
    """ ToDo: DocString """
    return "delete_user_accounts"
