SHELL := /bin/bash

manage_py := python app/manage.py

runserver:
	$(manage_py) runserver 0:8000

runcelery:
	celery -A booksharing worker -l info

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

shell_plus:
	$(manage_py) shell_plus --print-sql

flake8:
	flake8 app/

generate_data:
	$(manage_py) generate_data 50

rungunicorn:
	gunicorn booksharing.wsgi --workers=5 --bind 0.0.0.0:8000 --chdir=/home/andrey/booksharing/app --timeout=30 --max-requests=10000
