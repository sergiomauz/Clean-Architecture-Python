"""
    ToDo: DocString
"""

import uuid
from pydantic import validator

from core.common.errors import (
    DeferredValidator)


class GetPersonQuery(DeferredValidator):
    """ ToDo: DocString """
    uid: uuid.UUID

    @classmethod
    def new(cls, requested_uid: uuid):
        """ ToDo: DocString """
        uid = requested_uid

        new_instance = cls.create_instance(uid = uid)

        return new_instance.validate()
