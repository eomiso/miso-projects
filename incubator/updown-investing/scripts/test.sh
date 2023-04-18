#!/bin/bash

set -e
set -x

export PYTHONPATH=./app
coverage run -m pytest tests "${@}"
