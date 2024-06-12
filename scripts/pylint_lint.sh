#!/bin/bash
#
# Run PyLint with specific plugins loaded and message template

echo
echo "-------- PyLint Lint --------"
echo

# Lint
poetry run pylint \
  --disable='C0301, R0903, R0801, W0603' \
  --load-plugins pylint_pytest \
  --source-roots=./src \
  --output-format=colorized \
  --msg-template='Rule: {msg_id} - Position: [{line},{column}] -  {msg}' \
  ./src ./tests

echo
echo "--------------------------------"
echo