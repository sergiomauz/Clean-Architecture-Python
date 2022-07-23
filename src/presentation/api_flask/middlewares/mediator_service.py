# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
# pylint: disable=c-extension-no-member

"""
    ToDo: DocString
"""

import sys
from mediatr import Mediator
from dependency_injector import containers, providers

class MediatorContainer(containers.DeclarativeContainer):
    """ ToDo: DocString """
    mediator_service = providers.Singleton(
        Mediator
    )


def wire_mediator(module_name: str):
    """ ToDo: DocString """
    mediator_container = MediatorContainer()
    mediator_container.wire(modules = [sys.modules[module_name]])
