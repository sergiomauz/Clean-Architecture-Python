# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

class CreatePersonCommandDto:
    def __init__(self, request_body: dict):
        self.name = request_body["name"]
        self.last_name = request_body["last_name"]
