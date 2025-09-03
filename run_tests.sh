#!/bin/bash
# Simple test runner that actually works

# Add current directory to Python path
export PYTHONPATH=.

echo "Running KRISPER tests..."
python3 test_krisper.py || exit 1

echo -e "\nRunning Bio_Poetica tests..."
python3 test_bio_poetica.py || exit 1

echo -e "\n✅ All tests passed!"