#!/bin/sh

# # Wait for Docker to be ready.
# docker_ready=0
#
# while [ $docker_ready -eq 0 ]; do
#   echo "INFO: Checking if Docker is ready."
#   docker ps 2>&1 > /dev/null && docker_ready=1
#   sleep 1
# done

pytest -v tests
