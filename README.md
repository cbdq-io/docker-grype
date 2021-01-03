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

Tested on Ubuntu.  The file [examples/docker-compose.yml](examples/docker-compose.yml) contains
an example configuration that will test the `hello-world:latest` image.

This could be used by running the command (in the same directory as the
`docker-compose.yml` file):

```
docker-compose run grype
```
