# For more information:
# https://flask-migrate.readthedocs.io/en/latest/

cd src
flask db upgrade -d domain/persistence/main/migrations
