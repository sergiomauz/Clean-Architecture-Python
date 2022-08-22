"""
    ToDo: DocString
"""
from typing import Any
from pydantic import validator
from common.validators import DeferredValidator
from common.utils import Messages


class CreatePersonCommand(DeferredValidator):
    """ ToDo: DocString """
    name: str
    last_name: str

    @classmethod
    def new(cls, request: Any):
        """ ToDo: DocString """
        body = request.json
        name = body["name"]
        last_name = body["last_name"]
        new_instance = cls.create_instance(name = name, last_name = last_name)

        return new_instance.validate()

    @validator("name")
    def name_must_have_more_than_2_chars(cls, value):
        """ ToDo: DocString """
        assert len(value) > 2, Messages.MORE_THAN_2_CHARS

        return value

    @validator("last_name")
    def last_name_must_have_more_than_2_chars(cls, value):
        """ ToDo: DocString """
        assert len(value) > 2, Messages.MORE_THAN_2_CHARS

        return value
