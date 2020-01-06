venv:
	python3 -m venv venv

activate:
	bash -c "venv/bin/activate"

environ:
	bash -c "set -o allexport; source .env; set +o allexport;"