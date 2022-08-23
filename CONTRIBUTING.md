# Contributing

## Testing

We use [pytest-bdd](https://pypi.org/project/pytest-bdd/) for testing and these
tests are executed by a
[GitHub workflow](https://github.com/cbdq-io/docker-grype/actions) which must
pass before a pull request can be merged.

In the tests we have these following scenarios:

| Scenario | Fixed Only | Add CPEs if None |
| -------- | ---------- | ---------------- |
| A        | Yes        | No               |
| B        | Yes        | Yes              |
| C        | No         | No               |
| D        | No         | Yes              |

## Release Process

When a PR is merged back to the `main` this creates a new release, therefore
the merged branch should be set (in `Makefile`) after agreeing what the new
version number should be (following [SemVer](https://semver.org/)
guidelines).

After updating the version number then the following command should be
executed:

`make bump_version`

This will do the following steps:

- Generate the `CHANGELOG.md` file.
- Add the new file to Git and commit the file.
- Create a new tag on the Git repository.
