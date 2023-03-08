GRYPE_VERSION = 0.59.0
TAG = 1.20.8

all: shellcheck lint build test

build:
	docker build -f docker-grype/Dockerfile \
	  --no-cache \
	  -t ghcr.io/cbdq-io/docker-grype:$(TAG) \
	  -t ghcr.io/cbdq-io/docker-grype:latest \
	  -t ghcr.io/cbdq-io/docker-grype:unstable \
	  -t docker-grype:$(TAG) \
	  -t docker-grype:latest \
	  --build-arg GRYPE_VERSION=$(GRYPE_VERSION) \
          --quiet \
	  docker-grype

bump_version: changelog
	git add .
	git commit -m "chg: doc: Release $(TAG), !minor"

changelog:
	UNRELEASED_VERSION_LABEL=$(TAG) gitchangelog > CHANGELOG.md

clean:
	docker compose -f tests/resources/docker-compose.yml down -t 0
	docker compose -f tests/resources/docker-compose-self-test.yml down -t 0

cleanall: clean
	docker system prune --force --volumes

lint:
	yamllint -s .
	flake8
	bandit --ini setup.cfg -r .
	docker run --rm -i hadolint/hadolint < docker-grype/Dockerfile

push_latest:
	docker push ghcr.io/cbdq-io/docker-grype:$(TAG)
	docker push ghcr.io/cbdq-io/docker-grype:latest

push_unstable:
	docker push ghcr.io/cbdq-io/docker-grype:unstable

shellcheck:
	shellcheck docker-grype/docker-grype-cmd.sh

tag:
	git tag $(TAG)

test:
	GRYPE_VERSION=$(GRYPE_VERSION) docker compose -f tests/resources/docker-compose.yml up -d --wait docker grype
	GRYPE_VERSION=$(GRYPE_VERSION) PYTHONPATH=.:docker-grype pytest --cov -o cache_dir=/tmp/.pycache -v tests
	GRYPE_VERSION=$(GRYPE_VERSION) docker compose -f tests/resources/docker-compose.yml exec -T docker docker build -t docker-grype:latest --build-arg GRYPE_VERSION=$(GRYPE_VERSION) --quiet ./docker-grype
	GRYPE_VERSION=$(GRYPE_VERSION) docker compose -f tests/resources/docker-compose.yml run --rm sut

test-gh:
	GRYPE_VERSION=$(GRYPE_VERSION) docker compose -f tests/resources/docker-compose.yml up -d --wait docker grype
	GRYPE_VERSION=$(GRYPE_VERSION) PYTHONPATH=.:docker-grype pytest --cov -o cache_dir=/tmp/.pycache -v tests
	GRYPE_VERSION=$(GRYPE_VERSION) docker compose -f tests/resources/docker-compose.yml exec -T docker docker build -t docker-grype:latest --build-arg GRYPE_VERSION=$(GRYPE_VERSION) --quiet ./docker-grype
	GRYPE_VERSION=$(GRYPE_VERSION) docker compose -f tests/resources/docker-compose.yml run --rm sut${SCENARIO}
