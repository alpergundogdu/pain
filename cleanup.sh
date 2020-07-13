#!/bin/bash
set -euo pipefail

echo "Formatting scripts..."
find *.py pain/ -type f -name "*.py" | xargs poetry run isort
find *.py pain/ -type f -name "*.py" | xargs poetry run autopep8 -i

echo "Running tests ..."
poetry run pylint_runner --disable=C -v
