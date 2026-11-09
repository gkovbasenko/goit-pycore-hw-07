# goit-pycore-hw-07

Advanced address book with birthdays, CLI commands, and comprehensive unit tests.

Built on OOP entities: `Field`, `Name`, `Phone`, `Birthday`, `Record`, and `AddressBook` with a command-line interface.

## Instructions

### Setup

```bash
# Enter the project directory
cd goit-pycore-hw-07

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

### Run the Application

```bash
# Start the CLI assistant
python3 -m hw07.main
```

### Run Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/address_book/test_birthday.py -v

# Run specific test class
pytest tests/address_book/test_commands.py::TestAddContactCommand -v
```

### Available Commands

- `add <name> <phone>` — Create contact or add phone to existing
- `change <name> <phone>` — Add phone to existing contact
- `phone <name>` — Show contact's phones
- `all` — Display all contacts
- `add-birthday <name> <date>` — Add birthday (DD.MM.YYYY format)
- `show-birthday <name>` — Show specific contact's birthday
- `birthdays` — Show upcoming birthdays (next 7 days)
- `hello` — Greeting
- `close` / `exit` — Exit application

### Requirements

- Python 3.10+
- No external dependencies
