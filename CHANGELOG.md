# Changelog


## 1.21.8

### Changes

* Bump Grype version from 0.69.1 to 0.73.1. [Ben Dalling]

### Fix

* Increment release to fix 1.21.7 overwrite. [Ben Dalling]

### Other

* Build(deps): bump urllib3 from 2.0.6 to 2.0.7. [dependabot[bot]]

  Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.0.6 to 2.0.7.
  - [Release notes](https://github.com/urllib3/urllib3/releases)
  - [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)
  - [Commits](https://github.com/urllib3/urllib3/compare/2.0.6...2.0.7)

  ---
  updated-dependencies:
  - dependency-name: urllib3
    dependency-type: direct:production
  ...

* Build(deps): bump gitpython from 3.1.35 to 3.1.37. [dependabot[bot]]

  Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.35 to 3.1.37.
  - [Release notes](https://github.com/gitpython-developers/GitPython/releases)
  - [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES)
  - [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.35...3.1.37)

  ---
  updated-dependencies:
  - dependency-name: gitpython
    dependency-type: direct:production
  ...


## 1.21.7 (2023-10-04)

### Changes

* Bump the version of Grype from 0.67.0 to 0.69.1. [Ben Dalling]

### Other

* Build(deps): bump urllib3 from 2.0.2 to 2.0.6. [dependabot[bot]]

  Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.0.2 to 2.0.6.
  - [Release notes](https://github.com/urllib3/urllib3/releases)
  - [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)
  - [Commits](https://github.com/urllib3/urllib3/compare/2.0.2...2.0.6)

  ---
  updated-dependencies:
  - dependency-name: urllib3
    dependency-type: direct:production
  ...


## 1.21.6 (2023-09-13)

### Changes

* Bump Grype version from 0.66.0 to 0.67.0. [Ben Dalling]

### Other

* Build(deps): bump gitpython from 3.1.34 to 3.1.35. [dependabot[bot]]

  Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.34 to 3.1.35.
  - [Release notes](https://github.com/gitpython-developers/GitPython/releases)
  - [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES)
  - [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.34...3.1.35)

  ---
  updated-dependencies:
  - dependency-name: gitpython
    dependency-type: direct:production
  ...

* Build(deps): bump gitpython from 3.1.32 to 3.1.34. [dependabot[bot]]

  Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.32 to 3.1.34.
  - [Release notes](https://github.com/gitpython-developers/GitPython/releases)
  - [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES)
  - [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.32...3.1.34)

  ---
  updated-dependencies:
  - dependency-name: gitpython
    dependency-type: direct:production
  ...


## 1.21.5 (2023-08-31)

### Changes

* Bump Grype from 0.64.0 to 0.66.0. [Ben Dalling]

### Other

* Build(deps): bump gitpython from 3.1.31 to 3.1.32. [dependabot[bot]]

  Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.31 to 3.1.32.
  - [Release notes](https://github.com/gitpython-developers/GitPython/releases)
  - [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES)
  - [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.31...3.1.32)

  ---
  updated-dependencies:
  - dependency-name: gitpython
    dependency-type: direct:production
  ...


## 1.21.4 (2023-07-17)

### New

* Unfixed CVE-2023-36632 (II). [Ben Dalling]

* Unfixed CVE-2023-36632. [Ben Dalling]

### Changes

* Bump Grype version from 0.63.1 to 0.64.0. [Ben Dalling]

### Fix

* Correct issue when "Severity" is stored in related issues. [Ben Dalling]


## 1.21.3 (2023-07-02)

### Changes

* Bump Grype version from 0.62.3 to 0.63.1. [Ben Dalling]

* Bump Anchore Grype from 0.62.1 to 0.62.3. [Ben Dalling]

* Bump Anchore Grype version from 0.62.1 to 0.62.3. [Ben Dalling]

### Fix

* Update the Docker installation method on the image. [Ben Dalling]


## 1.21.1 (2023-05-26)

### Changes

* Bump Anchore Grype from 0.62.0 to 0.62.1. [Ben Dalling]


## 1.21.0 (2023-05-22)

### New

* Add --by-cve flags. [Ben Dalling]

### Changes

* Bump Anchore Grype from 0.61.1 to 0.62.0. [Ben Dalling]

### Fix

* GHSA-p782-xgp4-8hr8 no longer found in any test scenario. [Ben Dalling]

* GHSA-83g2-8m93-v3w7 no longer found in any test scenario. [Ben Dalling]

* Update docker/login-action version tag. [Ben Dalling]


## 1.20.10 (2023-04-26)

### Changes

* Bump the underlying Grype version from 0.59.0 to 0.61.1. [Ben Dalling]

### Fix

* Add GHSA-vvpx-j8f3-3w6h to the allowed list. [Ben Dalling]


## 1.20.9 (2023-03-09)

### Changes

* Bump Grype version from 0.56.0 to 0.59.0. [Ben Dalling]

### Fix

* Correct false reporting of if fixed vulnerabilities are being checked. [Ben Dalling]

* Remove libperl5.32 from the build (CVE-2020-16156). [Ben Dalling]

* CVE-2022-2097 is no longer found. [Ben Dalling]

* Add vulnerabilities to the allowed list for Grype itself. [Ben Dalling]

* Make CLI interpretation more flexible. [Ben Dalling]


## 1.20.8 (2023-01-30)

### Changes

* Bump Grype version from 0.55.0 to 0.56.0. [Ben Dalling]

### Fix

* CVE-2015-5237 & CVE-2021-22570 are resolved. [Ben Dalling]


## 1.20.7 (2023-01-05)

### Changes

* Bump Grype from 0.54.0 to 0.55.0. [Ben Dalling]

### Fix

* Resolve GHSA-r9hx-vwmv-q579/CVE-2022-40897. [Ben Dalling]


## 1.20.6 (2022-12-20)

### Changes

* Bump Grype version from 0.53.1 to 0.54.0. [Ben Dalling]

### Fix

* Remove CVE-2021-46848 from the non-fixed, allowed vulnerability list. [Ben Dalling]


## 1.20.5 (2022-12-12)

### Changes

* Migrate from Docker Hub to GitHub Container Registry. [Ben Dalling]

* Bump Grype from 0.52.0 to 0.53.1. [Ben Dalling]

### Other

* Build(deps): bump certifi from 2022.9.24 to 2022.12.7. [dependabot[bot]]

  Bumps [certifi](https://github.com/certifi/python-certifi) from 2022.9.24 to 2022.12.7.
  - [Release notes](https://github.com/certifi/python-certifi/releases)
  - [Commits](https://github.com/certifi/python-certifi/compare/2022.09.24...2022.12.07)

  ---
  updated-dependencies:
  - dependency-name: certifi
    dependency-type: direct:production
  ...


## 1.20.4 (2022-11-15)

### Changes

* Bump underlying Grype version from 0.50.2 to 0.52.0. [Ben Dalling]


## 1.20.3 (2022-10-18)

### Changes

* Bump Grype to 0.51.0. [Ben Dalling]


## 1.20.2 (2022-09-23)

### Changes

* Bump the underlying version of Grype from 0.50.1 to 0.50.2. [Ben Dalling]


## 1.20.1 (2022-09-19)

### Changes

* Bump the underlying Anchore Grype version from 0.49.0 to 0.50.1. [Ben Dalling]

### Other

* Bug: fix: Remove vulnerabilities from scenarios that are no longer found. [Ben Dalling]

* Doc: fix: Correct CONTRIBUTING.md. [Ben Dalling]

* Build(deps): bump mako from 1.1.3 to 1.2.2. [dependabot[bot]]

  Bumps [mako](https://github.com/sqlalchemy/mako) from 1.1.3 to 1.2.2.
  - [Release notes](https://github.com/sqlalchemy/mako/releases)
  - [Changelog](https://github.com/sqlalchemy/mako/blob/main/CHANGES)
  - [Commits](https://github.com/sqlalchemy/mako/commits)

  ---
  updated-dependencies:
  - dependency-name: mako
    dependency-type: direct:production
  ...


## 1.20.0 (2022-09-08)

### New

* Add the ADD_CPES_IF_NONE option. [Ben Dalling]

### Changes

* Bump underlying Grype version from 0.48.0 to 0.49.0. [Ben Dalling]

* Bump the version of Grype from 0.40.1 to 0.47.0. [Ben Dalling]

### Fix

* Ensure allowed bugs are registered as found. [Ben Dalling]

### Other

* Bump the version of Grype from 0.47.0 to 0.48.0. [Ben Dalling]


## 1.19.3 (2022-06-28)

### New

* Add the Bandit analyzer. [Ben Dalling]

### Changes

* Bump Grype version from 0.40.0 to 0.40.1. [Ben Dalling]

### Fix

* Implement Code Climate improvements. [Ben Dalling]

* Bump Grype version from 0.39.0 to 0.40.0. [Ben Dalling]


## 1.19.2 (2022-06-15)

### Changes

* Update non-fixed allowed vulnerability list. [Ben Dalling]

* Bump the version of Anchore Grype from 0.37.0 to 0.39.0. [Ben Dalling]


## 1.19.1 (2022-05-17)

### Changes

* Bump the version of Anchore Grype from 0.35.0 to 0.37.0. [Ben Dalling]

### Fix

* No longer finding CVE-2022-21698, CVE-2022-24778 or GHSA-8v99-48m9-c8pm in the scan. [Ben Dalling]

* Add CVE-2022-29458 to non-fixed allowed list. [Ben Dalling]


## 1.19.0 (2022-04-28)

### Changes

* Bump Grype version from 0.34.7 to 0.35.0. [Ben Dalling]

### Fix

* Add GHSA-8v99-48m9-c8pm to the allowed list. [Ben Dalling]

### Other

* Build(deps): bump paramiko from 2.7.2 to 2.10.1. [dependabot[bot]]

  Bumps [paramiko](https://github.com/paramiko/paramiko) from 2.7.2 to 2.10.1.
  - [Release notes](https://github.com/paramiko/paramiko/releases)
  - [Changelog](https://github.com/paramiko/paramiko/blob/main/NEWS)
  - [Commits](https://github.com/paramiko/paramiko/compare/2.7.2...2.10.1)

  ---
  updated-dependencies:
  - dependency-name: paramiko
    dependency-type: direct:production
  ...


## 1.18.0 (2022-03-29)

### Changes

* Bump image of Grype from 0.34.6 to 0.34.7. [Ben Dalling]

* Add GHSA-c3xm-pvg7-gh7r, GHSA-fgv8-vj5c-2ppq & GHSA-q3j5-32m5-58c2 to the allowed list. [Ben Dalling]

* Bump version of Anchore Grype from 0.34.3 to 0.34.6. [Ben Dalling]

### Fix

* Update allowed vulnerabilities list. [Ben Dalling]

* Simply build with the latest Python 3 Docker image. [Ben Dalling]

* Attempt to fix CVE-2022-0778. [Ben Dalling]


## 1.17.0 (2022-03-18)

### Changes

* Bump the Grype version from 0.33.0 to 0.34.3. [Ben Dalling]

### Fix

* Fix build process to ensure requested version is installed. [Ben Dalling]


## 1.16.0 (2022-02-24)

### Changes

* Bump Python version from 3.10.1 to 3.10.2. [Ben Dalling]

* Ensure a specific version (0.33.0) of Grype is installed. [Ben Dalling]


## 1.15.0 (2022-01-21)

### New

* Add ShellCheck to CI. [Ben Dalling]

### Changes

* Bump Grype version from 0.31.1 to 0.32.0. [Ben Dalling]

* Add test scenarios for with/without only fixed. [Ben Dalling]

* Update from ancient versions of Docker in documentation. [Ben Dalling]

### Fix

* Still run when not using only-fixed. [Ben Dalling]


## 1.14.1 (2022-01-14)

### Changes

* Bump Grype version from 0.28.0 to 0.31.1. [Ben Dalling]

### Fix

* Stop shell diagnosic message appearing on the console. [Ben Dalling]


## 1.14.0 (2021-12-23)

### Changes

* Anchore Grype 0.28.0 is available. [Ben Dalling]

### Fix

* Fix issues with tagging at release time. [Ben Dalling]


## 1.13.0 (2021-12-17)

### Changes

* Bump the base image to python:3.10.1. [Ben Dalling]

* New verion of Grype (0.27.3) is available. [Ben Dalling]

### Fix

* GHSA-c3xm-pvg7-gh7r no longer present. [Ben Dalling]


## 1.12.0 (2021-12-02)

### New

* Add the ONLY_FIXED flag. [Ben Dalling]


## 1.11.1 (2021-11-18)

### Changes

* Bump Grype from 0.25.0 to 0.25.1. [Ben Dalling]


## 1.11.0 (2021-11-16)

### Changes

* Bump the version of Grype from 0.24.1 to 0.25.0. [Ben Dalling]

### Fix

* GHSA-25xm-hr59-7c27 no longer being detected. [Ben Dalling]


## 1.10.0 (2021-11-15)

### Changes

* Bump expected Grype version from 0.24.0 to 0.24.1. [Ben Dalling]

* Bump Grype version from 0.23.0 to 0.24.0. [Ben Dalling]

### Fix

* Add to the VULNERABILITIES_ALLOWED_LIST. [Ben Dalling]


## 1.9.0 (2021-10-20)

### Changes

* Bump Grype version from 0.17.0 to 0.23.0. [Ben Dalling]

### Fix

* Resolve vulnerability CVE-2021-41617. [Ben Dalling]

* Resolve vulnerabilities CVE-2021-22945 & CVE-2021-22946. [Ben Dalling]

* Bump base image from python:3.9.6 to python:3.10.0. This resolves the following vulnerabilities CVE-2021-3711, CVE-2021-3712 & CVE-2021-35940. [Ben Dalling]


## 1.8.0 (2021-09-01)

### Changes

* Bump the Grype version from 0.15.0 to 0.17.0. [Ben Dalling]

### Fix

* Add CVE-2021-29921 to VULNERABILITIES_ALLOWED_LIST. [Ben Dalling]

* Remove CVE-2019-25013 from VULNERABILITIES_ALLOWED_LIST. [Ben Dalling]


## 1.7.2 (2021-07-17)

### Changes

* Bump base Python image to latest stable (3.9.6). [Ben Dalling]

* Bump expected Grype version from 0.13.0 to 0.15.0. [Ben Dalling]


## 1.7.1 (2021-07-05)

### Changes

* Bump base (Python) image from 3.9.4 to 3.9.5. [Ben Dalling]

### Fix

* Remove CVE-2021-20231, CVE-2021-20232 and CVE-2021-20305 from the allowed list. [Ben Dalling]


## 1.7.0 (2021-06-09)

### New

* Add CVE-2021-33574 to the allowed list. [Ben Dalling]

### Changes

* Minor documentation additions and corrections. [Ben Dalling]

* Bump Grype version from 0.12.1 to 0.13.0. [Ben Dalling]

### Other

* Build(deps): bump urllib3 from 1.26.4 to 1.26.5. [dependabot[bot]]

  Bumps [urllib3](https://github.com/urllib3/urllib3) from 1.26.4 to 1.26.5.
  - [Release notes](https://github.com/urllib3/urllib3/releases)
  - [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)
  - [Commits](https://github.com/urllib3/urllib3/compare/1.26.4...1.26.5)

  ---
  updated-dependencies:
  - dependency-name: urllib3
    dependency-type: direct:production
  ...


## 1.6.0 (2021-05-31)

### Changes

* Bump Grype version from 0.11.0 to 0.12.1. [Ben Dalling]

### Fix

* Resolve CVE-2021-3517. [Ben Dalling]

* Resolve CVE-2018-20225, CVE-2018-25011, CVE-2018-25014, CVE-2020-36328 & CVE-2020-36329. [Ben Dalling]


## 1.5.2 (2021-05-04)

### Fix

* Correct lint issue in Dockerfile. [Ben Dalling]

* Bump the expected version of Grype tp 0.11.0. [Ben Dalling]

* Bump base Docker image for 3.9.4. [Ben Dalling]


## 1.5.1 (2021-04-12)

### Changes

* Add CVE-2021-20305 to the accepted risks. [Ben Dalling]


## 1.5.0 (2021-04-12)

### Changes

* Grype updated from 0.8.0 to 0.9.0. [Ben Dalling]

### Fix

* CVE-2021-3177 no longer being idendified as a vulnerability. [Ben Dalling]

* Sort out the template for pull requests. [Ben Dalling]

### Other

* Build(deps): bump urllib3 from 1.26.3 to 1.26.4. [dependabot[bot]]

  Bumps [urllib3](https://github.com/urllib3/urllib3) from 1.26.3 to 1.26.4.
  - [Release notes](https://github.com/urllib3/urllib3/releases)
  - [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)
  - [Commits](https://github.com/urllib3/urllib3/compare/1.26.3...1.26.4)

* Build(deps): bump pyyaml from 5.3.1 to 5.4. [dependabot[bot]]

  Bumps [pyyaml](https://github.com/yaml/pyyaml) from 5.3.1 to 5.4.
  - [Release notes](https://github.com/yaml/pyyaml/releases)
  - [Changelog](https://github.com/yaml/pyyaml/blob/master/CHANGES)
  - [Commits](https://github.com/yaml/pyyaml/compare/5.3.1...5.4)


## 1.4.1 (2021-03-23)

### Changes

* Bump base image from Python 3.8 to 3.9.2. [Ben Dalling]

### Fix

* Add CVE-2021-20231 and CVE-2021-20232 to the whitelist. [Ben Dalling]


## 1.4.0 (2021-03-21)

### Changes

* Bump Grype version from 0.7.0 to 0.8.0. [Ben Dalling]

### Fix

* CVE-2018-20225 no longer an issue. [Ben Dalling]

* Purge config durng autoremove. [Ben Dalling]

### Other

* Build(deps): bump urllib3 from 1.26.2 to 1.26.3. [dependabot[bot]]

  Bumps [urllib3](https://github.com/urllib3/urllib3) from 1.26.2 to 1.26.3.
  - [Release notes](https://github.com/urllib3/urllib3/releases)
  - [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)
  - [Commits](https://github.com/urllib3/urllib3/compare/1.26.2...1.26.3)


## 1.3.4 (2021-03-04)

### Changes

* Update Drone CI example. [Ben Dalling]

### Fix

* Correct the number of columns in the vulnerability report. [Ben Dalling]


## 1.3.3 (2021-03-04)

### Fix

* Correct example code highlighting. [Ben Dalling]

### Other

* Build(deps): bump cryptography from 3.3.1 to 3.3.2. [dependabot[bot]]

  Bumps [cryptography](https://github.com/pyca/cryptography) from 3.3.1 to 3.3.2.
  - [Release notes](https://github.com/pyca/cryptography/releases)
  - [Changelog](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst)
  - [Commits](https://github.com/pyca/cryptography/compare/3.3.1...3.3.2)


## 1.3.2 (2021-02-06)

### New

* Add Drone CI (Kubernetes pipeline) example. [Ben Dalling]

### Fix

* Stop dublicate vulnerabilitity reports. [Ben Dalling]


## 1.3.1 (2021-01-30)

### New

* Document persisting the Grype DB. [Ben Dalling]

### Changes

* Docker Compose example testing on MacOS. [Ben Dalling]

### Fix

* Remove CVE-2020-29363 and add CVE-2021-3177 to the allowed list. [Ben Dalling]


## 1.3.0 (2021-01-28)

### New

* Add the SHOW_ALL_VULNERABILITIES option. [Ben Dalling]

### Changes

* Documentation updates. [Ben Dalling]

* Update the Grype version from 0.6.1 to 0.7.0. [Ben Dalling]

### Fix

* Remove tests link section as this is handled in GitHub well enough. [Ben Dalling]

* Avoid DL3005 in hadolint. [Ben Dalling]

### Other

* Update issue templates. [Ben Dalling]

* Create CODE_OF_CONDUCT.md. [Ben Dalling]


## 1.2.0 (2021-01-19)

### New

* Warn if an entry in allowed list is not found in the scan. [Ben Dalling]


## 1.1.2 (2021-01-19)

### New

* Added CVE-2019-25013 to the allowed list. [Ben Dalling]

### Fix

* Resolve CVE-2020-27843 & CVE-2020-27844. [Ben Dalling]


## 1.1.1 (2021-01-09)

### Fix

* Correct the example Docker Compose. [Ben Dalling]


## 1.1.0 (2021-01-09)

### New

* All the user to login to Docker. [Ben Dalling]

* YAML Lint Check. [Ben Dalling]


## 1.0.3 (2021-01-03)

### Fix

* Allow CI build to be skipped. [Ben Dalling]

* Resolve bad link issue. [Ben Dalling]

* Migrate from GitFlow to GitHub Flow. [Ben Dalling]


## 1.0.1 (2021-01-03)

### New

* Enable continuous deployment. [Ben Dalling]


## 1.0.0 (2021-01-03)

### New

* Add documentaion on options. [Ben Dalling]

* Create automated change log mechanism. [Ben Dalling]

* Add Docker Compose example. [Ben Dalling]

* Implement CI. [Ben Dalling]

* Implement an allowed list. [Ben Dalling]

* Create a Docker image for Grype and verify the version (0.6.1). [Ben Dalling]


