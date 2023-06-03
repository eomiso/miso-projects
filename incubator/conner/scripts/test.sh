#!/bin/bash

set -e
set -x

export PYTHONPATH=./app
coverage run --rcfile ./pyproject.toml -m pytest tests "${@}"
coverage report --fail-under 95 --show-missing
