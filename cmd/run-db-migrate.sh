# For more information:
# https://flask-migrate.readthedocs.io/en/latest/

read -p "Migration's name: " name
cd src
flask db migrate -d domain/persistence/main/migrations -m "$name"
