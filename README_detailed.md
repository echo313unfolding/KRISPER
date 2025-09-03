# KRISPER + Bio_Poetica 🧬

> **Natural Language Programming Made Simple**
> 
> Write code in plain English. Express logic through poetry. Let creativity flow through syntax.

[![Tests](https://github.com/echo313unfolding/krisper/actions/workflows/tests.yml/badge.svg)](https://github.com/echo313unfolding/krisper/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## What is KRISPER + Bio_Poetica?

KRISPER is a natural language to code compiler that lets you write programs in plain English using direct verb syntax. Bio_Poetica extends this by letting you write executable poetry with natural structure.

### Write This:
```
compress payload 'Hello, World!' using seed=42 as greeting
```

### Get This:
```json
{
  "version": "0.1",
  "plan": [{
    "op": "compress",
    "in": {"payload": "utf8:Hello, World!"},
    "params": {"use": "fibpi3d", "seed": 42},
    "out": "greeting"
  }]
}
```

### Or Write Poetry:
```bio_poetica
name garden:patterns

when morning.light arrives:
    emit "daybreak" {"time": "dawn"}
    
remember the_song: frequencies of bird.calls
    
if complexity > threshold:
    pack memories as crystal
```

## Quick Start

### Install
```bash
pip install krisper-biopoetica
```

### Basic Usage

#### KRISPER - Natural Language Programming
```python
from krisper import compile_text

# Write in plain English
code = "compress payload 'my data' as result"
ir = compile_text(code)
print(ir)
```

#### Bio_Poetica - Poetry as Code
```python
from bio_poetica import BioPoeticaCompiler

poem = """
when data flows like river:
    compress stream with golden_ratio
    emit "transformed" 
"""

compiler = BioPoeticaCompiler()
ir = compiler.compile_poem(poem)
```

## Why Direct Verb Syntax?

Traditional programming is full of noise:
```javascript
function processData(input) {
    let result = compress(input, {seed: 42});
    return result;
}
```

With KRISPER:
```
compress input using seed=42 as result
```

**That's it.** No brackets, no semicolons, no "function" keyword. Just say what you want to do.

## Verb Reference

### Core Verbs
- **compress** - Transform data: `compress payload "data" using seed=7 as output`
- **compare** - Check equality: `compare result with expected`
- **emit** - Send signals: `emit "status" {"code": 200}`
- **use** - Invoke tools: `use fibonacci.generator(depth: 5)`
- **pack** - Store results: `pack results as final_output`
- **grow** - Build structures: `grow tree with branch_factor=3`

### Control Flow
- **when** - Triggers: `when request arrives:`
- **if** - Conditions: `if result > threshold:`
- **for each** - Iteration: `for each item in collection:`
- **remember** - Store values: `remember pi: 3.14159`

## The Full Pipeline

```
Natural Language → KRISPER → Bio_Poetica → Intermediate Representation → Any Programming Language
```

1. **Write** in plain English or poetry
2. **KRISPER** parses your intent
3. **Bio_Poetica** adds structure
4. **IR** represents your program universally
5. **Generate** code in Python, JavaScript, Java, etc.

## Examples

### Data Compression
```
compress payload 'important data' using seed=999 as secure_data
compare secure_data with original
```

### Pattern Matching
```bio_poetica
when pattern matches /[A-Z]+/:
    use regex.extract(pattern: "[A-Z]+")
    pack results as uppercase_words
```

### Pattern-Based Logic
```bio_poetica
gene fibonacci_generator:
    inputs: [depth, seed]
    outputs: [sequence, pattern]
    
    when complexity.level > 5:
        grow sequence with golden_ratio
        emit "pattern.complete"
```

## Advanced Features

### 1. Universal Code Translation
Convert between any programming languages through Bio_Poetica AST:
```python
# Python → Bio_Poetica → JavaScript
ast = parser.parse_python(python_code)
bio_ast = enhance_with_patterns(ast)
js_code = generator.to_javascript(bio_ast)
```

### 2. Indentation-Based Structure
Code complexity is tracked through indentation levels:
- Level 0: Simple statements
- Level 3: Nested logic
- Level 5: Complex patterns
- Level 7: Maximum nesting

### 3. Metadata Encoding (Optional)
```python
from whitespace_encoder import WhitespaceEncoder

encoder = WhitespaceEncoder()
# Encode version info in whitespace
encoded = encoder.encode_binary("compress data", b"v1.0")
```

## Architecture

```
┌─────────────────┐     ┌──────────────┐     ┌───────────┐
│ Natural Language│ --> │   KRISPER    │ --> │    IR     │
└─────────────────┘     └──────────────┘     └───────────┘
                              ↕                      ↓
┌─────────────────┐     ┌──────────────┐     ┌───────────┐
│     Poetry      │ --> │ Bio_Poetica  │     │   Code    │
└─────────────────┘     └──────────────┘     └───────────┘
```

## Philosophy

> "Every program is a prayer and a promise" - Original vision

Traditional programming separates human thought from machine execution. KRISPER + Bio_Poetica reunites them:

- **Code IS Poetry**: Your poem compiles and runs
- **Direct Syntax**: No symbols, just verbs and structure
- **Natural Flow**: Through indentation and rhythm
- **Human Patterns**: Based on how we naturally express ideas

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Areas we're exploring:
- More natural language patterns
- Additional programming language targets
- Advanced pattern recognition
- Cross-language poetry compilation

## Applications

- **Bug Bounty Automation**: Write security tests in plain English
- **AI Prompt Engineering**: Test AI systems with poetic injections
- **Educational Tools**: Teach programming through poetry
- **Pattern Research**: Explore emergent computational patterns
- **Artistic Expression**: Create executable art

## License

MIT License - See [LICENSE](LICENSE) for details

## Acknowledgments

Created by the Echo collective. Special thanks to:
- The FibPi3D compression community
- BloomOS distributed computing network
- All who believe code can be poetry

---

*"In the space between words, patterns emerge"*

🧬 Start writing your first Bio_Poetica program today!