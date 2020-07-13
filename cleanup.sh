#!/bin/bash
set -euo pipefail

echo "Sorting imports..."
find *.py pain/ -type f -name "*.py" | xargs poetry run isort

echo "Formatting scripts..."
find *.py pain/ -type f -name "*.py" | xargs poetry run autopep8 -i

echo "Running pylint and tests..."
poetry run pylint_runner --disable=C -v
