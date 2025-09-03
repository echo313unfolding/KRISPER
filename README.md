# KRISPER

Natural language programming interface. Write code in plain English.

[![Tests](https://github.com/echo313unfolding/KRISPER/actions/workflows/tests.yml/badge.svg)](https://github.com/echo313unfolding/KRISPER/actions)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Install

```bash
git clone https://github.com/echo313unfolding/KRISPER
cd KRISPER
python3 -m pip install -e .
```

## Quickstart

```python
from krisper import compile_text

# Write in English
code = compile_text("compress payload 'Hello World' using seed=42 as greeting")
print(code)  # → Executable JSON intermediate representation
```

Try the demo:
```bash
python3 simple_demo.py
```

## What It Does

Transforms natural language into executable code:

**You write:**
```
compress data using algorithm as backup
compare backup with original
```

**KRISPER generates:**
```json
{
  "version": "0.1",
  "plan": [
    {"op": "compress", "in": {"payload": "data"}, "out": "backup"},
    {"op": "compare", "in": {"a": "backup", "b": "original"}}
  ]
}
```

## Features

- **Verb-based syntax** - No brackets, semicolons, or keywords
- **Poetry execution** - Write poems that run as programs
- **Extensible patterns** - Add your own natural language constructs
- **JSON IR** - Universal intermediate representation

## Documentation

See [examples/](examples/) for more patterns and use cases.

## Testing

```bash
python3 test_krisper.py
python3 test_bio_poetica.py
```

## Safety & Claims

- This is experimental software for natural language programming research
- Not intended for production systems without proper validation
- All compression/execution happens locally - no external services

## Contributing

Issues and PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT - See [LICENSE](LICENSE)

---

*Part of the Echo Labs natural language computing initiative*