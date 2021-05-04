FROM python:3.9.4

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1

# hadolint ignore=DL3008
RUN apt-get clean \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       apt-transport-https \
       ca-certificates \
       curl \
       gnupg-agent \
       software-properties-common \
    && wget -qO /tmp/debian.key https://download.docker.com/linux/debian/gpg \
    && apt-key add /tmp/debian.key \
    && add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/debian \
       $(lsb_release -cs) \
       stable" \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       docker-ce docker-ce-cli containerd.io \
    && apt-get purge -y \
       libbluetooth3 \
       libbluetooth-dev \
       libc-dev-bin \
       libopenjp2-7 \
       libp11-kit-dev \
       libpq5 \
       libpq-dev \
       libpython2.7-minimal \
       libpython2.7-stdlib \
       linux-libc-dev \
       python2.7 \
       python2.7-minimal \
    && apt-get -y autoremove --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && wget -qO - https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin

COPY docker-grype-cmd.sh /usr/local/bin/docker-grype-cmd.sh
COPY parse-grype-json.py /usr/local/bin/parse-grype-json.py

CMD ["/usr/local/bin/docker-grype-cmd.sh"]
