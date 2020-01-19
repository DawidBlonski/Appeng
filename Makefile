venv:
	python3 -m venv venv

activate:
	bash -c "source venv/bin/activate"


environ:
	bash -c "set -o allexport; source .env; set +o allexport;"

superuser:
	python backend/manage.py createsuperuser

migration:
	python backend/manage.py makemigrations
	python backend/manage.py migrate

run:
	python backend/manage.py runserver

test:
	python backend/manage.py test users

up:
	docker-compose up