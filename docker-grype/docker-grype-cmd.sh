#!/bin/sh

if [ -z "$IMAGE_NAME" ]; then
  echo 'ERROR: The IMAGE_NAME environment variable is not set.'
  exit 2
fi

if [ -z "$TOLERATE" ]; then
  export TOLERATE='medium'
fi

echo "INFO: Vulnerability toleration: $TOLERATE"

/usr/local/bin/grype $IMAGE_NAME -o json -v | /usr/local/bin/parse-grype-json.py
