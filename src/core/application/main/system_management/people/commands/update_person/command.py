# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=missing-class-docstring
# pylint: disable=import-error

"""
    ToDo: DocString
"""

from typing import Any
import uuid


class UpdatePersonCommand:
    def __init__(self, request: Any):
        self.uid = uuid.UUID(request.json["uid"])
        self.name = request.json["name"]
        self.last_name = request.json["last_name"]

        self.endpoint = request.url
        self.method = request.method
        self.remote_ip = request.remote_addr
