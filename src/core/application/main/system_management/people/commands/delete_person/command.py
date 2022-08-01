"""
    ToDo: DocString
"""

import uuid
from typing import Any, List
from pydantic import validator

from core.common.validators import (
    DeferredValidator)


class DeletePersonCommand(DeferredValidator):
    """ ToDo: DocString """
    uids: List[str]

    @classmethod
    def new(cls, request: Any):
        """ ToDo: DocString """
        uids = request.json["uids"]

        new_instance = cls.create_instance(uids = uids)

        return new_instance.validate()
