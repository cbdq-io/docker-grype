# docker-grype
Wrap Anchore Grype Inside Docker

## Examples

### Docker Compose

Tested on Ubuntu.  The file [examples/docker-compose.yml](examples/docker-compose.yml) contains
an example configuration that will test the `hello-world:latest` image.

This could be used by running the command (in the same directory as the
`docker-compose.yml` file):

```
docker-compose run grype
```
