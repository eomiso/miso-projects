#!/bin/bash

help_message() {
  echo "Usage: Run each application with python"
  echo
  echo "Options:"
  echo " -h, help            Show help message"
  echo " -m, --mvc           Run the MVC application"
}

if [[ $# -eq 0 ]]; then
    help_message
    exit 0
fi

if [[ $# -gt 0 ]]; then
  case "$1" in
  -h | --help)
    help_message
    exit 0
    ;;
  -m | --mvc)
    PYTHONPATH="./src" python ./src/mvc/main.py
    exit 0
    ;;
  -p | --mvp)
    PYTHONPATH="./src" python ./src/mvp/main.py
    exit 0
    ;;
  *)
    echo "Unknown option: $1"
    exit 1
    ;;
  esac
fi
