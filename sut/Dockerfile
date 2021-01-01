FROM docker-grype:latest

WORKDIR /work

COPY sut-entrypoint.sh /usr/local/bin/sut-entrypoint.sh
COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

ENTRYPOINT ["/usr/local/bin/sut-entrypoint.sh"]
