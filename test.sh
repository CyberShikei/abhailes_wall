#!/bin/bash

# Ensure the script stops on the first error
set -e

export PYTHONPATH=$(pwd)

#export TESTS_DIR=$(pwd)/src/tests/*

# Run all tests using unittest
# python -m unittest discover -s src/tests -p 'test_*.py'

# Run all tests using pytest
pytest src/tests

# Optional: Print success message if all tests pass
echo "All tests ran successfully."
