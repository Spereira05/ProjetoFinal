docker.build:
	docker-compose build --force-rm

docker.start:
	docker-compose up -d

install:
	poetry install

activate: install
	poetry shell

start: activate
	poetry run