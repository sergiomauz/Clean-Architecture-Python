"""
    ToDo: DocString
"""
from .systemmanagement.people import people
from .systemmanagement.useraccountgroups import user_account_groups
from .systemmanagement.useraccounts import user_accounts

API_V1 = "/api/v1"
module_system = f"{API_V1}/system"

def start_routes(app):
    """ ToDo: DocString """
    app.register_blueprint(people, url_prefix = f"{module_system}/people")
    app.register_blueprint(user_accounts, url_prefix = f"{module_system}/userAccounts")
    app.register_blueprint(user_account_groups, url_prefix = f"{module_system}/userAccountGroups")
