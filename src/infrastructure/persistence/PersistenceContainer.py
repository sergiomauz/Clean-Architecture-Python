# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

from dependency_injector import containers, providers
from .postgresql.main.services.systemmanagement.PeopleService import PeopleService

class PersistenceContainer(containers.DeclarativeContainer):
    """ ToDo: DocString """

    people_service = providers.Singleton(
        PeopleService
    )
