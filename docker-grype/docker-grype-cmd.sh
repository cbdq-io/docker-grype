#!/bin/sh

set -e

GRYPE_ARGS='-o json -v'

if [ -z "$IMAGE_NAME" ]; then
  echo 'ERROR: The IMAGE_NAME environment variable is not set.'
  exit 2
fi

if [ ! -z "${DOCKER_USERNAME}" -a -z "${DOCKER_PASSWORD}" ]; then
  echo "ERROR: You must provide DOCKER_USERNAME and DOCKER_PASSWORD together."
  exit 2
elif [ -z "${DOCKER_USERNAME}" -a ! -z "${DOCKER_PASSWORD}" ]; then
  echo "ERROR: You must provide DOCKER_USERNAME and DOCKER_PASSWORD together."
  exit 2
fi

if [ -z "$TOLERATE" ]; then
  export TOLERATE='medium'
fi

if [ ! -z "$ONLY_FIXED" -a $ONLY_FIXED -eq "1" ]; then
  GRYPE_ARGS="${GRYPE_ARGS} --only-fixed"
fi

docker_available=0
attempts=5
sleep_time=1

while [ $docker_available -ne 1 ]; do
  docker ps > /dev/null 2>&1

  if [ $? -ne 0 ]; then
    echo "WARN: Waiting ${sleep_time} seconds before checking Docker status again (${attempts} remaining attempts)"
    sleep $sleep_time
    sleep_time=$(( sleep_time += $sleep_time ))
    attempts=$(( attempts -= 1 ))

    if [ $attempts -eq 0 ]; then
      echo "ERROR: Unable to connect to Docker"
      exit 1
    fi
  else
    docker_available=1
  fi
done

if [ ! -z "${DOCKER_USERNAME}" ]; then
  echo "INFO: Logging into Docker with provided credentials"
  echo "${DOCKER_PASSWORD}" | docker login --password-stdin \
                                --username "${DOCKER_USERNAME}" \
                                "${DOCKER_SERVER}"
fi

/usr/local/bin/grype $IMAGE_NAME $GRYPE_ARGS | /usr/local/bin/parse-grype-json.py
