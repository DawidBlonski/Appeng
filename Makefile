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
	python backend/manage.py test answers


up:
	docker-compose up

redis_cmd:
	docker exec -it appeng_redis_1 sh

postgres_cmd:
	docker exec -it eng-app sh

