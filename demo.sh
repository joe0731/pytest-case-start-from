#!/bin/bash
# demonstration script for pytest-start-from plugin

echo "=========================================="
echo "pytest-start-from Plugin Demo"
echo "=========================================="
echo ""

# make sure the plugin is installed
echo "Installing plugin in development mode..."
pip install -e . > /dev/null 2>&1

echo ""
echo "=========================================="
echo "1. Normal pytest execution (no plugin)"
echo "=========================================="
pytest test_example.py -v

echo ""
echo "=========================================="
echo "2. Start from test_third"
echo "=========================================="
pytest test_example.py --start-from test_third -v

echo ""
echo "=========================================="
echo "3. Start from class method"
echo "=========================================="
pytest test_example.py --start-from test_class_second -v

echo ""
echo "=========================================="
echo "4. Pattern matching with substring"
echo "=========================================="
pytest test_example.py --start-from "parameters" -v

echo ""
echo "=========================================="
echo "Demo completed!"
echo "=========================================="
