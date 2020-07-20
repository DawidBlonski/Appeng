venv:
	python3 -m venv venv

activate:
	bash -c "source venv/bin/activate"

environ:
	bash "set -o allexport; source .env; set +o allexport;"

superuser:
	python manage.py createsuperuser

migration:
	python manage.py makemigrations
	python manage.py migrate
fake_migration:
	python manage.py migrate --fake
run:
	python manage.py runserver

test:
	python manage.py test answers

format:
	black .

up:
	docker-compose up

redis_cmd:
	docker exec -it appeng_redis_1 sh

postgres_cmd:
	docker exec -it eng-app sh

