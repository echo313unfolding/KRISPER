# KRISPER Universal - Supporting All Languages

## Current Architecture
```
English → KRISPER Compiler → JSON IR → Executors
```

## Universal Architecture
```
English → KRISPER Compiler → JSON IR → Language Generators → Any Language
```

## Language Generators

### Python Generator
```python
def generate_python(ir):
    if ir["op"] == "compress":
        return f"compressed = compress({ir['in']['payload']})"
    elif ir["op"] == "filter":
        return f"filtered = [x for x in {ir['in']['data']} if {ir['params']['where']}]"
```

### JavaScript Generator
```python
def generate_javascript(ir):
    if ir["op"] == "compress":
        return f"const compressed = compress({ir['in']['payload']})"
    elif ir["op"] == "filter":
        return f"const filtered = {ir['in']['data']}.filter(x => {ir['params']['where']})"
```

### SQL Generator
```python
def generate_sql(ir):
    if ir["op"] == "filter":
        return f"SELECT * FROM {ir['in']['data']} WHERE {ir['params']['where']}"
```

## Example Usage

KRISPER input:
```
load csv file "sales.csv" as data
filter data where amount > 1000 as high_sales
sort high_sales by date descending
```

Generates Python:
```python
import pandas as pd
data = pd.read_csv("sales.csv")
high_sales = data[data['amount'] > 1000]
high_sales = high_sales.sort_values('date', ascending=False)
```

Generates JavaScript:
```javascript
const data = await loadCSV("sales.csv");
const high_sales = data.filter(row => row.amount > 1000);
high_sales.sort((a, b) => b.date - a.date);
```

Generates SQL:
```sql
CREATE TEMP TABLE high_sales AS
SELECT * FROM sales WHERE amount > 1000 ORDER BY date DESC;
```

## Implementation Plan

1. **Extend IR Schema** - Add type hints and context
2. **Create Language Generators** - One per target language
3. **VS Code Integration** - Choose output language in settings
4. **Language-Specific Patterns** - Idioms for each language

## Benefits

- Write once in English, generate to any language
- No need to remember syntax for multiple languages
- Consistent logic across all platforms
- AI assistants can help with natural language, not syntax