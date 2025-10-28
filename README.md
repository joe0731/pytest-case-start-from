# pytest-start-from

A pytest plugin that allows you to start test execution from a specific test case, skipping all tests before it.

## Features

- ✅ Start test execution from any test case using `--start-from` or `-sf` option
- ✅ Pattern matching similar to pytest's `-k` option
- ✅ Support for substring matching
- ✅ Support for logical operators: `and`, `or`, `not`
- ✅ Works with test functions, test methods, and test classes
- ✅ Easy to install and use

## Installation

### Development mode (for local testing)

```bash
pip install -e .
```

### Regular installation

```bash
pip install .
```

## Quick Start

```bash
# skip all tests before test_third
pytest --start-from test_third

# pattern matching with substring
pytest --start-from "third"

# match test in a class
pytest --start-from "TestClass::test_method"
```

## Usage Examples

### Basic Usage

```bash
# start from a specific test
pytest --start-from test_fourth test_example.py

# use with verbose output
pytest --start-from test_second -v

# combine with other pytest options
pytest --start-from test_third -v -s --tb=short
```

### Pattern Matching

```bash
# substring match
pytest --start-from "class_second"

# logical operators
pytest --start-from "parameters and a"
pytest --start-from "first or second"
pytest --start-from "test not class"
```

## How It Works

1. The plugin hooks into pytest's test execution flow
2. Before each test runs, it checks if the test name matches the specified pattern
3. All tests before the first match are marked as SKIPPED
4. Once the first matching test is found, all subsequent tests run normally

## Documentation

For detailed usage instructions, see [USAGE.md](USAGE.md)

## Use Cases

- **Debugging**: Skip passing tests and start from the failing test
- **Incremental Testing**: Continue from where tests were interrupted
- **Development**: Focus on specific tests during feature development
- **CI/CD Optimization**: Resume test execution from a specific point

## Requirements

- Python >= 3.7
- pytest >= 6.0.0

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.
