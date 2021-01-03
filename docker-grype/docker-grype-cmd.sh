#!/bin/sh

if [ -z "$IMAGE_NAME" ]; then
  echo 'ERROR: The IMAGE_NAME environment variable is not set.'
  exit 2
fi

if [ -z "$TOLERATE" ]; then
  export TOLERATE='medium'
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

/usr/local/bin/grype $IMAGE_NAME -o json -v | /usr/local/bin/parse-grype-json.py
