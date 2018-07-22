#!/bin/ash

echo
echo "RUNNING TESTS..."
echo
echo "TESTING STATIC TYPING (mypy)..."
mypy --strict -m bsdnumber.converter
echo "DONE"
echo
echo "RUNNING UNIT TESTS (pytest)..."
pytest
echo "DONE"
echo
