TAG = 1.0.0

all: lint build test
	echo $(TAG)

build:
	docker-compose -f docker-grype/docker-compose.test.yml build grype sut
	docker build -f docker-grype/Dockerfile -t docker-grype:$(TAG) docker-grype
	docker-compose -f docker-grype/docker-compose.test.yml build sut

clean:
	docker-compose -f docker-grype/docker-compose.test.yml down -t 0

cleanall:
	docker system prune --force --volumes

lint:
	docker run --rm -i hadolint/hadolint < docker-grype/Dockerfile

ps:
	docker-compose -f docker-grype/docker-compose.test.yml ps

test:
	docker-compose -f tests/resources/docker-compose.yml up -d
	pytest -o cache_dir=/tmp/.pycache -v tests
