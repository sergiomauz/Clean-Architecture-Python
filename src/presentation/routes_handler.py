"""
    ToDo: DocString
"""


from core.common.utils import Constants
from .api.routes.system_management import (
    people, user_account_groups, user_accounts)


class RoutesHandler:
    """ ToDo: DocString """
    def start_routes(self, app):
        """ ToDo: DocString """
        module_system = f"{Constants.API_V1}/system"

        app.register_blueprint(people,
                               url_prefix = f"{module_system}/people")
        app.register_blueprint(user_accounts,
                               url_prefix = f"{module_system}/userAccounts")
        app.register_blueprint(user_account_groups,
                               url_prefix = f"{module_system}/userAccountGroups")
