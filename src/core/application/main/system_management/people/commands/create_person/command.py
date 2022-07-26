# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=no-self-argument

"""
    ToDo: DocString
"""

from typing import Any
from pydantic import BaseModel, validator

class CreatePersonCommand(BaseModel):
    name: str
    last_name: str

    @classmethod
    def new(cls, request: Any):
        """ ToDo: DocString """
        name = request.json["name"]
        last_name = request.json["last_name"]

        return cls(name = name, last_name = last_name)


    @validator("name")
    def name_must_have_more_than_3_chars(cls, value):
        """ ToDo: DocString """
        if len(value) < 3:
            raise ValueError("must have more than 3 chars")

        return value


    @validator("last_name")
    def last_name_must_have_more_than_3_chars(cls, value):
        """ ToDo: DocString """
        if len(value) < 3:
            raise ValueError("must have more than 3 chars")

        return value
