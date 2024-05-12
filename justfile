#!/usr/bin/env just --justfile

# Load from '.env' file
set dotenv-load

# List available commands
help:
    @just --justfile {{justfile()}} --list --unsorted

# PyLint
lint:
  # PyLint lint from ./src and ./tests
  ./scripts/pylint_lint.sh

# SQLFluff
lint_sql file="./queries":
  # Fix and lint
  ./scripts/sqlfluff_fix_and_lint.sh {{file}}

# Setup Elasticsearch
setup_elasticsearch:
  bash scripts/setup_elasticsearch.sh

# Create an Elasticsearch user in interactive mode
create_elasticsearch_user:
  bash scripts/create_elasticsearch_user.sh

# Test .env file
test_env_file:
  echo $TEST_ENV_VAR

# Execute PyTests under '/tests'
test:
    poetry run pytest

# Start Jupyter Lab with the Poetry Virtual Environment
jupy:
  poetry run jupyter lab