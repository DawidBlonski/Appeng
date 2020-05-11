venv:
	python3 -m venv venv

activate:
	bash -c "source venv/bin/activate"

environ:
	bash "set -o allexport; source .env; set +o allexport;"

superuser:
	python backend/manage.py createsuperuser

migration:
	python backend/manage.py makemigrations
	python backend/manage.py migrate
fake_migration:
	python backend/manage.py migrate --fake
run:
	python backend/manage.py runserver

test:
	python backend/manage.py test answers

format:
	black backend/.

up:
	docker-compose up

redis_cmd:
	docker exec -it appeng_redis_1 sh

postgres_cmd:
	docker exec -it eng-app sh

