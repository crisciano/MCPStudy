
startdev: venv dotenv compile sync sourceenv
# backend/sales/management/commands/runmcp.py
runmcp: dotenv
	npx @modelcontextprotocol/inspector http://127.0.0.1:8025/mcp/
# 	venv/bin/python backend/manage.py mcp_inspector --url http://127.0.0.1:8025/mcp
# 	venv/bin/python backend/manage.py mcp_inspector  --port 8025

sourceenv:
	set -e; source ./envvars;

dotenv:
	@echo "export DJANGO_SECRET_KEY=$(DJANGO_SECRET_KEY);" > ./envvars;

runserver: dotenv
	venv/bin/python backend/manage.py runserver 127.0.0.1:8025
# 	set -e; source ./envvars; \
	venv/bin/python backend/manage.py runserver 127.0.0.1:8025

migrations: dotenv
	venv/bin/python backend/manage.py makemigrations $(app);

migrate: dotenv
	venv/bin/python backend/manage.py migrate $(app) $(file);

loading:
	venv/bin/python backend/manage.py loaddata backend/initial_data

createsuperuser:
	venv/bin/python backend/manage.py createsuperuser

clean:
	venv/bin/python backend/manage.py flush

sync: venv
	venv/bin/pip-sync dev-requirements.txt requirements.txt

compile:
	venv/bin/pip-compile --no-emit-index-url
	venv/bin/pip-compile --no-emit-index-url dev-requirements.in

sync: venv
	venv/bin/pip-sync dev-requirements.txt requirements.txt

venv:
	test -d venv || python -m venv venv
	venv/bin/pip install --upgrade pip pip-tools