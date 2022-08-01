"""
    ToDo: DocString
"""

from dependency_injector import containers, providers
from infrastructure.persistence.postgresql.main.services.system_management.people import (
    PeopleService)
from presentation.startup import SettingsService


class PersistenceContainer(containers.DeclarativeContainer):
    """ ToDo: DocString """
    settings_service = providers.Singleton(
        SettingsService
    )

    people_service = providers.Singleton(
        PeopleService
        # settings_service
    )
