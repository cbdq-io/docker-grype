# docker-grype

Wrap [Anchore Grype](https://github.com/anchore/grype) Inside Docker

## Environment Variables

- `IMAGE_NAME` (_required_):  The name of the image to be scanned.
- `LOG_LEVEL` (default is `INFO`):  The log level for how much output to be provided.  Can be set to
  DEBUG, INFO, WARNING, ERROR or CRITICAL.
- `TOLERATE` (default is `Medium`): The level of severity to tolerate before giving a non-zero
  return code.  Valid values (in increasing order of severity) are `Unknown`, `Negligible`, `Low`,
  `Medium`, `High` or `Critical`.
- `VULNERABILITIES_ALLOWED_LIST` (optional): A comma separated list of vulnerabilities that are not to count against
  a failure (e.g. `CVE-2018-20225,CVE-2020-29363`).

## Examples

### Docker Compose

Tested on Ubuntu.  This snippet contains
an example configuration that will test the `hello-world:latest` image.

```YAML
---
version: "3"

services:
  docker:
    container_name: docker
    environment:
      DOCKER_TLS_CERTDIR: ""
    image: docker:18-dind
    privileged: yes
    volumes:
      - certs:/certs/client
      - ../..:/work
    working_dir: /work

  grype:
    container_name: grype
    depends_on:
      - docker
    environment:
      DOCKER_HOST: tcp://docker:2375
      DOCKER_TLS_CERTDIR: ""
      IMAGE_NAME: hello-world:latest
    image: cbdq/docker-grype:latest

volumes:
  certs:
```

This could be used by running the command (in the same directory as the
`docker-compose.yml` file):

```shell
docker-compose run grype
```
