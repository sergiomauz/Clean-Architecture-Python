# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

"""
    ToDo: DocString
"""

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from server.core.domain.main.systemmanagement.Person import Person

db = SQLAlchemy(app)

class PersonMap(db.Model, Person):
    id = Column(UUID, primary_key = True, index = True)
    name = Column(db.String(100))
    last_name = Column(db.String(100))

    def __init__(self, name, last_name):
        super().__init__()
        self.name = name
        self.last_name = last_name
