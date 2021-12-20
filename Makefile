TAG = 1.13.1

all: lint build test

build: changelog
	docker build -f docker-grype/Dockerfile --no-cache -t cbdq/docker-grype:$(TAG) -t cbdq/docker-grype:latest -t docker-grype:$(TAG) -t docker-grype:latest docker-grype

bump_version: changelog
	git add .
	git commit -m "chg: doc: Release $(TAG), !minor"

changelog:
	UNRELEASED_VERSION_LABEL=$(TAG) gitchangelog > CHANGELOG.md

clean:
	docker-compose -f tests/resources/docker-compose.yml down -t 0
	docker-compose -f tests/resources/docker-compose-self-test.yml down -t 0

cleanall: clean
	docker system prune --force --volumes

lint:
	yamllint -s .
	flake8 docker-grype/parse-grype-json.py
	pycodestyle -v tests
	docker run --rm -i hadolint/hadolint < docker-grype/Dockerfile

push:
	echo ${DOCKER_PASSWORD} | docker login --username ${DOCKER_USERNAME} --password-stdin
	docker push cbdq/docker-grype:$(TAG)
	docker push cbdq/docker-grype:latest

tag:
	git tag $(TAG)

test:
	docker-compose -f tests/resources/docker-compose.yml up -d docker grype
	pytest -o cache_dir=/tmp/.pycache -v tests
	docker-compose -f tests/resources/docker-compose.yml exec -T docker docker build -t docker-grype:latest ./docker-grype
	docker-compose -f tests/resources/docker-compose.yml run --rm -e 'VULNERABILITIES_ALLOWED_LIST=' sut
