# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

import os
import sys
from dotenv import load_dotenv
from mediatr import Mediator
from dependency_injector import containers, providers

class MediatorContainer(containers.DeclarativeContainer):
    """ ToDo: DocString """
    mediator_service = providers.Singleton(
        Mediator
    )


class SettingsService:
    """ ToDo: DocString """
    def __init__(self) -> None:
        """ ToDo: DocString """
        load_dotenv()
        self.__value = os.environ

    def get(self, key: str) -> str:
        """ ToDo: DocString """
        return self.__value[key]


def wire_mediator(module_name):
    """ ToDo: DocString """
    mediator_container = MediatorContainer()
    mediator_container.wire(modules = [sys.modules[module_name]])
