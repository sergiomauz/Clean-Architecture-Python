# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from dependency_injector import containers, providers
from settings import SettingsService
from .postgresql.main.services.systemmanagement.PeopleService import PeopleService

class PersistenceContainer(containers.DeclarativeContainer):
    """ ToDo: DocString """
    settings_service = providers.Singleton(
        SettingsService
    )

    people_service = providers.Singleton(
        PeopleService,
        settings_service
    )
