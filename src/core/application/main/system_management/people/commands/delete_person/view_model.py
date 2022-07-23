# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=missing-class-docstring
# pylint: disable=import-error

"""
    ToDo: DocString
"""

from core.common.models.jsonable import Jsonable

class DeletePersonVm(Jsonable):
    def __init__(self, were_deleted: bool):
        super().__init__()
        self.were_deleted = were_deleted
