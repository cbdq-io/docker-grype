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
       ca-certificates \
       curl \
       gnupg \
       software-properties-common \
    && install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
    && chmod a+r /etc/apt/keyrings/docker.gpg \
    && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt-get update \
    && apt-get upgrade -y \
       bash \
       libssl-dev \
    && apt-get install -y --no-install-recommends \
       docker-ce \
       docker-ce-cli \
       containerd.io \
       docker-buildx-plugin \
    && curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -d -b /usr/local/bin "v${GRYPE_VERSION}" \
    && apt-get purge -y \
       curl \
       libbluetooth3 \
       libbluetooth-dev \
       libc-dev-bin \
       libcurl3-gnutls \
       libcurl4 \
       libopenjp2-7 \
       libperl5.36 \
       libp11-kit-dev \
       libpq5 \
       libpq-dev \
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
