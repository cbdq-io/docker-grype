FROM python:3.11
ARG GRYPE_VERSION

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1
LABEL org.opencontainers.image.source=https://github.com/cbdq-io/docker-grype
LABEL org.opencontainers.image.description="Wrap Anchore Grype Inside Docker"
LABEL org.opencontainers.image.licenses=Apache-2.0

# hadolint ignore=DL3008
RUN apt-get clean \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       apt-transport-https \
       ca-certificates \
       curl \
       gnupg-agent \
       software-properties-common \
    && curl -so /tmp/debian.key https://download.docker.com/linux/debian/gpg \
    && apt-key add /tmp/debian.key \
    && add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/debian \
       $(lsb_release -cs) \
       stable" \
    && apt-get update \
    && apt-get upgrade -y libssl-dev \
    && apt-get install -y --no-install-recommends \
       bash \
       docker-ce \
       docker-ce-cli \
       containerd.io \
    && curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -d -b /usr/local/bin "v${GRYPE_VERSION}" \
    && apt-get purge -y \
       curl \
       libbluetooth3 \
       libbluetooth-dev \
       libc-dev-bin \
       libcurl3-gnutls \
       libcurl4 \
       libopenjp2-7 \
       libp11-kit-dev \
       libpq5 \
       libpq-dev \
       libpython2.7-minimal \
       libpython2.7-stdlib \
       libpython3.9-minimal \
       libwebp-dev \
       libxml2 \
       linux-libc-dev \
       openssh-client \
       python2.7 \
       python2.7-minimal \
    && apt-get -y autoremove --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip --no-cache-dir install -U 'setuptools>=65.5.1' \
    && pip uninstall -y pip

COPY docker-grype-cmd.sh /usr/local/bin/docker-grype-cmd.sh
COPY parse-grype-json.py /usr/local/bin/parse-grype-json.py
COPY pygrype /usr/local/lib/python3.11/pygrype

CMD ["/usr/local/bin/docker-grype-cmd.sh"]
