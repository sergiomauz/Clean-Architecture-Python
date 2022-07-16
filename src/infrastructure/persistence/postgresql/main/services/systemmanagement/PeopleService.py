"""
    ToDo: DocString
"""
from dependency_injector.wiring import inject, Provide
from settings import SettingsContainer

class PeopleService():
    """ ToDo: DocString """
    def __init__(self,) -> None:
        """ ToDo: DocString """

    @inject
    def sum(self, a_b, b_c, settings_service = Provide[SettingsContainer.settings_service]):
        """ ToDo: DocString """
        print(settings_service)
        return a_b + b_c
