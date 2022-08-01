"""
    ToDo: DocString
"""

from typing import Any
from pydantic import validator

from core.common.validators import (
    DeferredValidator)


class CreatePersonCommand(DeferredValidator):
    """ ToDo: DocString """
    name: str
    last_name: str

    @classmethod
    def new(cls, request: Any):
        """ ToDo: DocString """
        name = request.json["name"]
        last_name = request.json["last_name"]

        new_instance = cls.create_instance(name = name, last_name = last_name)

        return new_instance.validate()


    @validator("name")
    def name_must_have_more_than_3_chars(cls, value):
        """ ToDo: DocString """
        assert len(value) > 2, "Must have more than 3 chars."

        return value


    @validator("last_name")
    def last_name_must_have_more_than_3_chars(cls, value):
        """ ToDo: DocString """
        assert len(value) > 2, "Must have more than 3 chars."

        return value
