# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""
import os
from dotenv import load_dotenv
from dependency_injector import containers, providers

class SettingsService():
    """ ToDo: DocString """
    def __init__(self) -> None:
        """ ToDo: DocString """
        load_dotenv()
        self.__value = os.environ

    def get_value(self, key: str) -> str:
        """ ToDo: DocString """
        return self.__value[key]


class SettingsContainer(containers.DeclarativeContainer):
    """ ToDo: DocString """
    settings_service = providers.Singleton(
        SettingsService
    )
