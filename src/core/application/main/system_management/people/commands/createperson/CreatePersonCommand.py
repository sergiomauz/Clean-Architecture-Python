# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""

class CreatePersonCommand:
    def __init__(self, request):
        self.name = request.json["name"]
        self.last_name = request.json["last_name"]
