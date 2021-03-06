VIRTUAL_ENV ?= venv
SOURCE_DIRS = apps civic_europe cms tests

.PHONY: all
all: help

.PHONY: help
help:
	@echo civic-europe development tools
	@echo
	@echo It will either use a exisiting virtualenv if it was entered
	@echo before or create a new one in the same directory.
	@echo
	@echo usage:
	@echo
	@echo "  make install          -- install dev setup"
	@echo "  make clean            -- delete node modules and venv"
	@echo "  make fixtures         -- load example data"
	@echo "  make server           -- start a dev server"
	@echo "  make watch            -- start a dev server and rebuild js and css files on changes"
	@echo "  make background       -- start background processes"
	@echo "  make test             -- tests on exiting database"
	@echo "  make test-lastfailed  -- run test that failed last"
	@echo "  make test-clean       -- test on new database"
	@echo "  make coverage         -- write coverage report to dir htmlcov"
	@echo "  make lint             -- lint javascript and python, check for missing migrations"
	@echo "  make po               -- create new po files from the source"
	@echo "  make mo               -- create new mo files from the translated po files"
	@echo "  make release          -- build everything required for a release"
	@echo

.PHONY: install
install:
	npm install --no-save
	npm run build
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv $(VIRTUAL_ENV); fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install --upgrade -r requirements/dev.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate

.PHONY: clean
clean:
	if [ -f package-lock.json ]; then rm package-lock.json; fi
	if [ -d node_modules ]; then rm -rf node_modules; fi
	if [ -d venv ]; then rm -rf venv; fi

.PHONY: fixtures
fixtures:
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata civic_europe/fixtures/site-dev.json
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata civic_europe/fixtures/users-dev.json
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata civic_europe/fixtures/projects-dev.json
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata civic_europe/fixtures/idea-dev.json


.PHONY: server
server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8002

.PHONY: watch
watch:
	trap 'kill %1' KILL; \
	npm run watch & \
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8002

.PHONY: background
background:
	$(VIRTUAL_ENV)/bin/python3 manage.py process_tasks

.PHONY: test
test:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db

.PHONY: test-lastfailed
test-lastfailed:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --last-failed

.PHONY: test-clean
test-clean:
	if [ -f test_db.sqlite3 ]; then rm test_db.sqlite3; fi
	$(VIRTUAL_ENV)/bin/py.test

.PHONY: coverage
coverage:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --cov --cov-report=html

.PHONY: lint
lint:
	EXIT_STATUS=0; \
	$(VIRTUAL_ENV)/bin/isort --diff -c $(SOURCE_DIRS) ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/flake8 $(SOURCE_DIRS) --exclude migrations,settings ||  EXIT_STATUS=$$?; \
	npm run lint --silent ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/python manage.py makemigrations --dry-run --check --noinput || EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

.PHONY: release
release: export DJANGO_SETTINGS_MODULE ?= civic_europe.settings.build
release:
	npm install --silent
	npm run build:prod
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements.txt -q
	$(VIRTUAL_ENV)/bin/python3 manage.py collectstatic --noinput -v0

.PHONY: make
make:
	@echo Hello dwarf planet!
