# aka_json

A Python module for robust JSON/JSON5 file handling with datataсlass support, custom encoders/decoders, and enhanced error handling.

---

## Features

- **JSON & JSON5 Support**: Read/write standard JSON and relaxed JSON5 files (comments, trailing commas).
- **Dataclass Integration**: Seamless serialization/deserialization using `dacite`.
- **Extended Type Support**: Auto-handling of `datetime`, `date`, `time`, and `bytes` objects.
- **Validation & Safety**: File extension checks, content type enforcement (dict/list), and encoding control.
- **Error Handling**: Custom exceptions (`FileExtensionError`, `ContentTypeError`, `FileOpenError`).
- **Formatting Control**: Customize indentation, ASCII encoding, key sorting, and file modes.
- **Context Managers**: Safe file handling using `with` statements.

---

## Installation

### Dependencies
Use this if you clone repository
```bash
pip install dacite json5
```

### Module Setup
Install via PyPi
```bash
pip install dacite json5
```

Or clone the repository:
```bash
git clone https://github.com/your-repo/aka_json.git
cd aka_json
```
Import classes directly into your project.

---

## Quick Start

### Basic JSON Operations
```python
from aka_json import JsonFile

# Create and write to a JSON file
with JsonFile("data.json", create_file=True) as file:
    file.write({"name": "Alice", "age": 30})

# Read data
data = JsonFile("data.json").read()
print(data)  # Output: {'name': 'Alice', 'age': 30}
```

### Dataclass Serialization
```python
from dataclasses import dataclass
from aka_json import JsonFile

@dataclass
class User:
    name: str
    age: int

# Write dataclass object
user = User("Bob", 25)
with JsonFile("user.json", create_file=True) as file:
    file.write(user)

# Read as dataclass
loaded_user = JsonFile("user.json").read_as_dataclass(User)
print(loaded_user)  # Output: User(name='Bob', age=25)
```

### JSON5 File Handling
```python
from aka_json import Json5File

# Write to JSON5 (supports relaxed syntax)
with Json5File("config.json5", create_file=True) as file:
    config = {
        "host": "localhost",  # Example comment
        "port": 8080,
    }
    file.write(config)
```

---

## Core Classes

| Class               | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `SimpleJsonFile`    | Base JSON handler (open/read/write/remove).                                 |
| `JsonFile`          | Adds dataclass support to `SimpleJsonFile`.                                 |
| `SimpleJson5File`   | Base JSON5 handler with relaxed syntax support.                             |
| `Json5File`         | Extends `SimpleJson5File` with dataclass integration.                       |

---

## Key Methods

### Common Operations
- `open(create_file=False)`: Open file (create if missing).
- `close(remove_file=False)`: Close file (optionally delete it).
- `read()`: Return JSON data as dict/list.
- `write(content)`: Write data to file (supports dataclasses).
- `read_as_dataclass(cls)`: Deserialize JSON into a dataclass object.
- `clear()`: Reset file to empty dict/list.

### Configuration
```python
file.set_options(
    content_type=ContentType.LIST,  # Dict/List structure
    coding=Coding.UTF8,            # Encoding
    indent=4,                      # Indentation
    sort_keys=True                  # Sort JSON keys
)
```

---

## Constants

### `ContentType`
- `DICT`: Treat file as dictionary (default).
- `LIST`: Treat file as list.

### `FileMode`
- Modes: `READ`, `WRITE`, `APPEND`, and binary variants.

### `Coding`
- Encodings: `UTF8`, `ASCII`, `GBK`, and 10+ others.

---

## Error Handling

```python
from aka_json import FileExtensionError, ContentTypeError

try:
    # Attempt to open non-JSON file
    file = JsonFile("data.txt")
except FileExtensionError as e:
    print(f"Error: {e}")  # "File data.txt has incorrect extension"
```

---

## License
MIT License. See `LICENSE` for details.