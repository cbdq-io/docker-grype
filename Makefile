TAG = 1.14.2

all: shellcheck lint build test

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

shellcheck:
	shellcheck docker-grype/docker-grype-cmd.sh

tag:
	git tag $(TAG)

test:
	docker-compose -f tests/resources/docker-compose.yml up -d docker grype
	pytest -o cache_dir=/tmp/.pycache -v tests
	docker-compose -f tests/resources/docker-compose.yml exec -T docker docker build -t docker-grype:latest ./docker-grype
	ONLY_FIXED=1 docker-compose -f tests/resources/docker-compose.yml run --rm -e 'VULNERABILITIES_ALLOWED_LIST=' sut
	docker-compose -f tests/resources/docker-compose.yml run --rm -e 'VULNERABILITIES_ALLOWED_LIST=CVE-2015-5237,CVE-2020-16156,CVE-2021-29921,CVE-2021-33560,CVE-2021-33574,CVE-2021-45960,CVE-2021-46143,CVE-2022-22822,CVE-2022-22823,CVE-2022-22824,CVE-2022-22825,CVE-2022-22826,CVE-2022-22827' sut
