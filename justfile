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

# Execute PyTests under '/tests'
test:
    poetry run pytest