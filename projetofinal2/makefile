.PHONY: install shell build down up makemigrations migrate createsuperuser

install:
	pip install poetry

shell:
	poetry shell

build:
	docker-compose build

down:
	docker-compose down

up: build
	docker-compose up

deploy-migrate: ## Run manage migrate
	python3 manage.py makemigrations
	python3 manage.py migrate

deploy-update: ## DEPLOY - Runs poetry update
	poetry update

test-super-user: ## TEST - Creates generic admin superuser
	poetry run python manage.py createsuperuser --username admin --email admin@example.com

test: ## TEST - Runs server on 8000
	poetry run python manage.py runserver





