TAG = 1.9.0

all: lint build test

build:
	docker build -f docker-grype/Dockerfile --no-cache -t cbdq/docker-grype:$(TAG) -t cbdq/docker-grype:latest -t docker-grype:$(TAG) -t docker-grype:latest docker-grype

bump_version:
	UNRELEASED_VERSION_LABEL=$(TAG) gitchangelog > CHANGELOG.md
	git add .
	git commit -m "chg: doc: Release $(TAG), !minor"
	git tag -a -m"v$(TAG)" $(TAG)

clean:
	docker-compose -f tests/resources/docker-compose.yml down -t 0

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

test:
	docker-compose -f tests/resources/docker-compose.yml up -d docker grype
	pytest -o cache_dir=/tmp/.pycache -v tests
	docker-compose -f tests/resources/docker-compose.yml exec -T docker \
	    docker build -t docker-grype:latest ./docker-grype
	docker-compose -f tests/resources/docker-compose.yml \
	  run -e 'LOG_LEVEL=DEBUG' \
              -e 'VULNERABILITIES_ALLOWED_LIST=CVE-2021-29921,CVE-2021-33574' sut
