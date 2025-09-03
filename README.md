<p align="center">
  <img src="krisper_readme_intro.svg" alt="KRISPER — English → IR → Execution" />
</p>

<p align="center">
  <strong>Natural language programming interface. Write code in plain English.</strong>
</p>

<p align="center">
  <a href="#install">Install</a> •
  <a href="#quickstart">Quick Start</a> •
  <a href="#features">Features</a> •
  <a href="#documentation">Docs</a> •
  <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/echo313unfolding/KRISPER/tests.yml?style=for-the-badge&logo=github&label=Tests&color=00F723" alt="Tests">
  <img src="https://img.shields.io/badge/Python-3.8+-00F723?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/github/license/echo313unfolding/KRISPER?style=for-the-badge&color=00F723" alt="License">
  <img src="https://img.shields.io/github/stars/echo313unfolding/KRISPER?style=for-the-badge&color=00F723" alt="Stars">
</p>

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

## 🚀 Demo

<p align="center">
  <img src="https://via.placeholder.com/600x400/0D1117/00F723?text=Demo+GIF+Coming+Soon" alt="KRISPER Demo" width="600">
</p>

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