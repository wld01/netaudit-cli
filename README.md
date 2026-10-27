# netaudit-cli

![CI](https://github.com/wld01/netaudit-cli/workflows/CI/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A simple, fast CLI tool to audit network configuration files (Cisco, Juniper, generic text formats).

## Features

- Parse and display raw network configuration files
- Extensible parser architecture for new config formats
- Rich terminal output with syntax highlighting
- GitHub Actions CI across Python 3.10+

## Architecture

```
netaudit-cli/
├── netaudit/            # Core package
│   ├── __init__.py      # Package metadata
│   ├── parser.py        # Configuration file parsing
│   └── cli.py           # Typer-based CLI entrypoint
├── tests/               # Unit tests (unittest)
├── .github/workflows/   # CI configuration
├── requirements.txt     # Runtime dependencies
└── LICENSE              # MIT License
```

## Installation

```bash
git clone https://github.com/wld01/netaudit-cli.git
cd netaudit-cli
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
# Inspect a configuration file
python -m netaudit.cli inspect router.cfg

# Get help
python -m netaudit.cli --help
```

## Running Tests

```bash
python -m unittest discover -s tests -v
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
