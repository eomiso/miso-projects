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

create_pyproject() {
  local name="$1" # Project name

cat<<EOF>pyproject.toml
[tool.poetry]
name = "${name}"
version = "0.1.0"
description = "Personal auto-trading application"
authors = ["Uiseop Eom <ytrtef@gmail.com>"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = ">=3.10,<3.11"
pydantic = "^1.10.7"
httpx = "^0.23.3"
anyio = "^3.6.2"

[tool.poetry.group.dev.dependencies]
ruff = "^0.0.261"
isort = "^5.12.0"
pre-commit = "^3.2.1"
black = "^23.3.0"
pytest = "^7.2.2"
fastapi = {extras = ["pytest"], version = "^0.95.0"}
coverage = "^7.2.2"
pytest-anyio = "^0.0.0"

[tool.ruff]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    # "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
]
ignore = [
    "E501",  # line too long, handled by black
    "B008",  # do not perform function calls in argument defaults
    "C901",  # too complex
]

[tool.isort]
# https://github.com/timothycrosley/isort
# https://github.com/timothycrosley/isort/wiki/isort-Settings
profile = "black"

[tool.black]
# https://github.com/psf/black
line-length = 88
isort = true
exclude = '''
/(
    \.git
  | \.mypy_cache
  | \.tox
  | venv
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''

[tool.poetry.build]
generate-setup-file = false

[settings.virtualenvs]
in-project = true

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
EOF
}

create_gitignore() {
cat<<EOF>.gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
.venv/
# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

poetry.toml

.DS_Store/
EOF
}

# Create README.md file
create_readme() {
cat<<EOF>README.md
# ${name}
EOF
}

create_poetry_toml() {
cat<<EOF>poetry.toml
[virtualenvs]
in-project = true
EOF
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
