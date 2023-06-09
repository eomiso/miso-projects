#!/bin/bash

set -e
set -x

curl -X GET http://localhost:3000

curl -X POST http://localhost:3000/hello \
-d '{"name": "John"}'
