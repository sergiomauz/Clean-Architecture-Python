# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods

"""
    ToDo: DocString
"""
import os
from dotenv import load_dotenv

class SettingsService():
    """ ToDo: DocString """
    def __init__(self) -> None:
        """ ToDo: DocString """
        load_dotenv()
        self.__value = os.environ

    def get(self, key: str) -> str:
        """ ToDo: DocString """
        return self.__value[key]
