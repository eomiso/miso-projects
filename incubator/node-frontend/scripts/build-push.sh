#!/usr/bin/env bash

set -e
set -x

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

docker buildx build --platform=linux/amd64,linux/arm64 -t eomiso/node-frontend:18 .

docker buildx build --platform=linux/amd64,linux/arm64 -t eomiso/node-frontend:latest .
docker build -t eomiso/node-frontend:latest .

docker push eomiso/node-frontend:18

docker push eomiso/node-frontend:18
