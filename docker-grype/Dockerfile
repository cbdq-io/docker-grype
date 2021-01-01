FROM python:3.8

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1

COPY requirements.txt /tmp/requirements.txt

# hadolint ignore=DL3008,DL3015
RUN apt-get update \
    && apt-get install -y \
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
    && apt-get install -y docker-ce docker-ce-cli containerd.io \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r /tmp/requirements.txt

RUN wget -qO - https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY docker-grype-cmd.sh /usr/local/bin/docker-grype-cmd.sh

CMD ["/usr/local/bin/docker-grype-cmd.sh"]
