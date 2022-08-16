"""
    ToDo: DocString
"""

from typing import Any
from pydantic import validator

from common.validators import (
    DeferredValidator)

from application.common.general import BasicSearchParameters


class SearchPeopleQuery(DeferredValidator):
    """ ToDo: DocString """
    basic_search_parameters: BasicSearchParameters

    @classmethod
    def new(cls, request: Any):
        """ ToDo: DocString """
        basic_search_parameters = BasicSearchParameters.new(request)

        new_instance = cls.create_instance(basic_search_parameters = basic_search_parameters)

        return new_instance.validate()
