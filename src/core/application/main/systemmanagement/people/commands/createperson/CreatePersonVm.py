# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

"""
    ToDo: DocString
"""
class CreatePersonVm():
    def __init__(self) -> None:
        self.id = None
        self.name = None
        self.last_name = None
        self.created_at = None
        self.modified_at = None

    @property
    def id(self):
        return self.id
    
    @property
    def name(self):
        return self.name

    @property
    def last_name(self):
        return self.last_name

    @property
    def created_at(self):
        return self.created_at

    @property
    def modified_at(self):
        return self.modified_at
    
    @id.setter
    def id(self, new_value):
        self.id = new_value
        
    @name.setter
    def name(self, new_value):
        self.name = new_value

    @last_name.setter
    def last_name(self, new_value):
        self.last_name = new_value

    @created_at.setter
    def created_at(self, new_value):
        self.created_at = new_value
        
    @modified_at.setter
    def modified_at(self, new_value):
        self.modified_at = new_value
