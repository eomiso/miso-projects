#!/bin/bash

version="0.0.1"

# Help message
help_message() {
  echo "Usage: create-poetry-api-server.sh [OPTIONS]"
  echo
  echo "Options:"
  echo "  -h, --help                   Show help message"
  echo "  -v, --version                Show script version"
  echo "  -n, --name <project_name>    Name of the project"
}

# Version message
version_message() {
  echo "Script version $version"
}

# Check if no arguments were passed
if [[ $# -eq 0 ]]; then
  help_message
  exit 0
fi
# Parse command-line arguments
if [[ $# -gt 0 ]]; then
  case "$1" in
  -h | --help)
    help_message
    exit 0
    ;;
  -v | --version)
    version_message
    exit 0
    ;;
  -n | --name)
    if [ "$2" = "" ]; then
      echo "Project name is required"
      exit 1
    fi
    create_pyproject "$2"
    create_poetry_toml
    create_gitignore
    exit 0
    ;;
  *)
    echo "Unknown option: $1"
    exit 1
    ;;
  esac
fi
