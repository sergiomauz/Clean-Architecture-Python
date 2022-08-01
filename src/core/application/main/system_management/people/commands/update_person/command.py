"""
    ToDo: DocString
"""

import uuid
from typing import Any
from pydantic import validator

from core.common.validators import (
    DeferredValidator)


class UpdatePersonCommand(DeferredValidator):
    """ ToDo: DocString """
    uid: uuid.UUID
    name: str
    last_name: str

    @classmethod
    def new(cls, request: Any):
        """ ToDo: DocString """
        uid = uuid.UUID(request.json["uid"])
        name = request.json["name"]
        last_name = request.json["last_name"]

        new_instance = cls.create_instance(uid = uid, name = name, last_name = last_name)

        return new_instance.validate()
