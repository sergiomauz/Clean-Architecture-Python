# For more information:
# https://flask-migrate.readthedocs.io/en/latest/

cd src/domain/persistence/main/flask_commands
flask db upgrade -d ../migrations
