GRYPE_VERSION = 0.40.1
TAG = 1.19.3

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
	GRYPE_VERSION=$(GRYPE_VERSION) ONLY_FIXED=1 docker-compose -f tests/resources/docker-compose.yml run --rm -e 'VULNERABILITIES_ALLOWED_LIST=GHSA-c3xm-pvg7-gh7r,GHSA-crp2-qrr5-8pq7,GHSA-fgv8-vj5c-2ppq,GHSA-q3j5-32m5-58c2' sut
	GRYPE_VERSION=$(GRYPE_VERSION) docker-compose -f tests/resources/docker-compose.yml run --rm -e 'VULNERABILITIES_ALLOWED_LIST=CVE-2015-20107,CVE-2015-5237,CVE-2019-8457,CVE-2020-16156,CVE-2021-22570,CVE-2021-29921,CVE-2021-33560,CVE-2021-3737,CVE-2022-0391,CVE-2022-0529,CVE-2022-0530,CVE-2022-1304,CVE-2022-1586,CVE-2022-1587,CVE-2022-29458,GHSA-c3xm-pvg7-gh7r,GHSA-crp2-qrr5-8pq7,GHSA-fgv8-vj5c-2ppq,GHSA-q3j5-32m5-58c2' sut
