"""
    ToDo: DocString
"""
import sys
from dependency_injector.wiring import inject, Provide
from settings import SettingsContainer

class PeopleService():
    """ ToDo: DocString """
    def __init__(self,) -> None:
        """ ToDo: DocString """
        settings_container = SettingsContainer()
        settings_container.wire(modules = [sys.modules[__name__]])

    @inject
    def sum(self, settings_service = Provide[SettingsContainer.settings_service])-> None:
        """ ToDo: DocString """
        print(settings_service)
        return 147
