#!/bin/sh

if [ -z "$IMAGE_NAME" ]; then
  echo 'ERROR: The IMAGE_NAME environment variable is not set.'
  exit 2
fi

/usr/local/bin/grype $IMAGE_NAME
