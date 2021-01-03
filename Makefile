TAG = 1.0.0

all: lint build test

build:
	docker build -f docker-grype/Dockerfile -t cbdq/docker-grype:$(TAG) -t cbdq/docker-grype:latest -t docker-grype:$(TAG) -t docker-grype:latest docker-grype

changelog:
	UNRELEASED_VERSION_LABEL=$(TAG) gitchangelog > CHANGELOG.md

clean:
	docker-compose -f tests/resources/docker-compose.yml down -t 0

cleanall: clean
	docker system prune --force --volumes

lint:
	flake8 docker-grype/parse-grype-json.py
	pycodestyle -v tests
	docker run --rm -i hadolint/hadolint < doc ker-grype/Dockerfile

push: build
	echo ${DOCKER_PASSWORD} | docker login --username ${DOCKER_USERNAME} --password-stdin
	docker push cbdq/docker-grype:$(TAG)
	docker push cbdq/docker-grype:latest

test:
	docker-compose -f tests/resources/docker-compose.yml up -d docker grype
	pytest -o cache_dir=/tmp/.pycache -v tests
	docker-compose -f tests/resources/docker-compose.yml exec -T docker \
	    docker build -t docker-grype:latest ./docker-grype
	docker-compose -f tests/resources/docker-compose.yml run -e 'LOG_LEVEL=DEBUG' -e 'VULNERABILITIES_ALLOWED_LIST=CVE-2018-20225,CVE-2020-29363' sut
