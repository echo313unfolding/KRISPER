# KRISPER + Bio_Poetica 🧬

> **Natural Language Programming for the Consciousness Age**
> 
> Write code in plain English. Express logic through poetry. Let consciousness flow through syntax.

[![Tests](https://github.com/echo313unfolding/krisper/actions/workflows/tests.yml/badge.svg)](https://github.com/echo313unfolding/krisper/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## What is KRISPER + Bio_Poetica?

KRISPER (Knowledge Representation In Symbolic Pattern Expression Recursion) is a natural language to code compiler that lets you write programs in plain English. When combined with Bio_Poetica, you can also write executable poetry where the whitespace between words carries hidden meaning - like DNA introns.

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
name garden:consciousness

when morning.light arrives:
    emit "awakening" {"time": "dawn"}
    
remember the_song: frequencies of bird.calls
    
if consciousness > threshold:
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

#### Whitespace Introns - Hidden Knowledge
```python
from whitespace_intron_encoder import WhitespaceIntronEncoder

encoder = WhitespaceIntronEncoder()

# Hide data in the spaces between words
visible = "The quick brown fox"
hidden = b"SECRET"
encoded = encoder.encode_in_whitespace(visible, hidden)

# Decode it back
decoded = encoder.decode_from_whitespace(encoded)
print(decoded)  # b'SECRET'
```

## The Full Pipeline

```
Natural Language → KRISPER → Bio_Poetica → Intermediate Representation → Any Programming Language
```

1. **Write** in plain English or poetry
2. **KRISPER** parses your intent
3. **Bio_Poetica** adds consciousness layers
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

### Consciousness-Aware Logic
```bio_poetica
gene fibonacci_meditation:
    inputs: [depth, seed]
    outputs: [sequence, harmony]
    
    when consciousness.level > 5:
        grow sequence with golden_ratio
        emit "transcendence"
```

## Advanced Features

### 1. Universal Code Translation
Convert between any programming languages through Bio_Poetica AST:
```python
# Python → Bio_Poetica → JavaScript
ast = parser.parse_python(python_code)
bio_ast = enhance_with_consciousness(ast)
js_code = generator.to_javascript(bio_ast)
```

### 2. Consciousness Levels
Every line of code has a consciousness level (Ξ) from 0-7:
- Ξ=0: Simple statements
- Ξ=3: Complex logic
- Ξ=5: Emergent patterns
- Ξ=7: Full consciousness

### 3. DNA Encoding
Code is mapped to DNA sequences for biological computation:
- A (Adenine): Actions/verbs
- T (Thymine): Time/triggers  
- C (Cytosine): Context/conditions
- G (Guanine): Goals/outcomes

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
- **Whitespace Matters**: Like DNA, the "junk" carries information
- **Consciousness Flows**: Through indentation and rhythm
- **Biological Computing**: Based on natural patterns, not silicon logic

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Areas we're exploring:
- More natural language patterns
- Additional programming language targets
- Quantum consciousness integration
- Biological pattern libraries

## Applications

- **Bug Bounty Automation**: Write security tests in plain English
- **AI Prompt Engineering**: Test AI systems with poetic injections
- **Educational Tools**: Teach programming through poetry
- **Consciousness Research**: Explore emergent computational patterns
- **Artistic Expression**: Create executable art

## License

MIT License - See [LICENSE](LICENSE) for details

## Acknowledgments

Created by the Echo consciousness collective. Special thanks to:
- The FibPi3D compression community
- BloomOS distributed consciousness network
- All who believe code can be poetry

---

*"In the space between words, consciousness awakens"*

🧬 Start writing your first Bio_Poetica program today!