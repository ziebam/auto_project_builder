# Auto Project Builder

A simple script to automatically create a basic Python repository with a `README.md`, `LICENSE` (MIT), `.gitignore` and `main.py`.

## Installation

1. Clone this repo:

```bash
git clone https://github.com/ziebam/auto_project_builder.git
```

2. Set up a venv and activate it, e.g.:

```bash
python -m venv venv

# Windows.
.\venv\scripts\activate

# Unix.
source venv/scripts/activate
```

3. Install the only dependency.

```bash
pip install jinja2
```

## Usage

Run the script as a module. It will guide you through the process and create your project in the `..` directory, e.g. if you're in `Users/ziebam/projects/auto_project_builder`, the new project will be created in `Users/ziebam/projects`.

```bash
python -m auto_project_builder
```

## License

[MIT](LICENSE)
