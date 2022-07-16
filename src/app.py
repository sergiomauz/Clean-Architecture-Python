"""
    ToDo: DocString
"""
import sys
from flask import Flask

from dependency_injector.wiring import inject, Provide

from infrastructure.persistence.PersistenceContainer import PersistenceContainer
from presentation.api.routes.start import start_routes



@inject
def imprimir(people_service = Provide[PersistenceContainer.people_service]) -> None:
    suma = people_service.sum(8 , 7)
    print(people_service)


app = Flask(__name__)

# Start routes
start_routes(app)

if __name__ == '__main__':
    persistence_container = PersistenceContainer()
    persistence_container.wire(modules = [sys.modules[__name__]])
    
    imprimir()
    
    app.run(debug = True)
