GRYPE_VERSION = 0.50.1
TAG = 1.20.1

all: shellcheck lint build test

build: changelog
	docker build -f docker-grype/Dockerfile \
	  --no-cache \
	  -t cbdq/docker-grype:$(TAG) \
	  -t cbdq/docker-grype:latest \
	  -t docker-grype:$(TAG) \
	  -t docker-grype:latest \
	  --build-arg GRYPE_VERSION=$(GRYPE_VERSION) \
          --progress plain \
	  docker-grype

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
	flake8
	docker run --rm -i hadolint/hadolint < docker-grype/Dockerfile

push:
	echo ${DOCKER_PASSWORD} | docker login --username ${DOCKER_USERNAME} --password-stdin
	docker push cbdq/docker-grype:$(TAG)
	docker push cbdq/docker-grype:latest

shellcheck:
	shellcheck docker-grype/docker-grype-cmd.sh

tag:
	git tag $(TAG)

test:
	GRYPE_VERSION=$(GRYPE_VERSION) docker-compose -f tests/resources/docker-compose.yml up -d docker grype
	GRYPE_VERSION=$(GRYPE_VERSION) pytest --cov -o cache_dir=/tmp/.pycache -v tests
	GRYPE_VERSION=$(GRYPE_VERSION) docker-compose -f tests/resources/docker-compose.yml exec -T docker docker build -t docker-grype:latest --build-arg GRYPE_VERSION=$(GRYPE_VERSION) ./docker-grype
	GRYPE_VERSION=$(GRYPE_VERSION) docker-compose -f tests/resources/docker-compose.yml run --rm sut

test-gh:
	GRYPE_VERSION=$(GRYPE_VERSION) docker-compose -f tests/resources/docker-compose.yml up -d docker grype
	GRYPE_VERSION=$(GRYPE_VERSION) pytest --cov -o cache_dir=/tmp/.pycache -v tests
	GRYPE_VERSION=$(GRYPE_VERSION) docker-compose -f tests/resources/docker-compose.yml exec -T docker docker build -t docker-grype:latest --build-arg GRYPE_VERSION=$(GRYPE_VERSION) ./docker-grype
	GRYPE_VERSION=$(GRYPE_VERSION) docker-compose -f tests/resources/docker-compose.yml run --rm sut${SCENARIO}
