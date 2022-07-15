"""
    ToDo: DocString
"""
from flask import Flask

from server.presentation.api.routes.systemmanagement.people import people
from server.presentation.api.routes.systemmanagement.useraccountgroups import user_account_groups

app = Flask(__name__)
app.register_blueprint(people)
app.register_blueprint(user_account_groups)

if __name__ == '__main__':
    app.run(debug=True)
