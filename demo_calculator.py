#!/usr/bin/env python3
"""
KRISPER Demo - Natural Language Calculator
Shows how plain English becomes executable code
"""

from krisper import compile_text
import json

class SimpleExecutor:
    """Execute basic math operations from KRISPER IR"""
    
    def __init__(self):
        self.memory = {}
    
    def execute(self, ir):
        """Execute KRISPER IR for math operations"""
        if isinstance(ir, str):
            ir = json.loads(ir)
            
        for op in ir.get('plan', []):
            operation = op['op']
            
            if operation == 'add':
                a = self._get_value(op['in'].get('a'))
                b = self._get_value(op['in'].get('b'))
                result = a + b
                
            elif operation == 'multiply':
                a = self._get_value(op['in'].get('a'))
                b = self._get_value(op['in'].get('b'))
                result = a * b
                
            elif operation == 'divide':
                a = self._get_value(op['in'].get('a'))
                b = self._get_value(op['in'].get('b'))
                result = a / b
                
            elif operation == 'subtract':
                a = self._get_value(op['in'].get('a'))
                b = self._get_value(op['in'].get('b'))
                result = a - b
                
            # Store result
            if op.get('out'):
                self.memory[op['out']] = result
                
        return result
    
    def _get_value(self, val):
        """Get numeric value from IR"""
        if isinstance(val, str):
            if val.startswith('num:'):
                return float(val[4:])
            elif val in self.memory:
                return self.memory[val]
        return float(val)

def demo():
    """Show off KRISPER's natural language power"""
    print("🧬 KRISPER: Write Math in Plain English!")
    print("=" * 50)
    
    # Extend KRISPER with math patterns
    original_compile = compile_text
    
    def compile_math(text):
        """Extended compiler with math operations"""
        # Try original patterns first
        try:
            return original_compile(text)
        except:
            pass
            
        # Math patterns
        import re
        
        # Pattern: "add X and Y as Z"
        match = re.match(r'add (\d+) and (\d+) as (\w+)', text)
        if match:
            return {
                "version": "0.1",
                "plan": [{
                    "op": "add",
                    "in": {"a": f"num:{match.group(1)}", "b": f"num:{match.group(2)}"},
                    "out": match.group(3)
                }]
            }
            
        # Pattern: "multiply X by Y as Z"
        match = re.match(r'multiply (\d+) by (\d+) as (\w+)', text)
        if match:
            return {
                "version": "0.1", 
                "plan": [{
                    "op": "multiply",
                    "in": {"a": f"num:{match.group(1)}", "b": f"num:{match.group(2)}"},
                    "out": match.group(3)
                }]
            }
            
        # Pattern: "X plus Y equals Z"
        match = re.match(r'(\d+) plus (\d+) equals (\w+)', text)
        if match:
            return {
                "version": "0.1",
                "plan": [{
                    "op": "add",
                    "in": {"a": f"num:{match.group(1)}", "b": f"num:{match.group(2)}"},
                    "out": match.group(3)
                }]
            }
            
        raise ValueError(f"Cannot parse: {text}")
    
    executor = SimpleExecutor()
    
    # Demo calculations
    examples = [
        "add 5 and 3 as sum",
        "multiply 7 by 8 as product",
        "42 plus 13 equals answer"
    ]
    
    for example in examples:
        print(f"\n📝 English: {example}")
        
        # Compile to IR
        ir = compile_math(example)
        print(f"🔄 IR: {json.dumps(ir, indent=2)}")
        
        # Execute
        result = executor.execute(ir)
        output_name = ir['plan'][0]['out']
        print(f"✅ Result: {output_name} = {result}")
    
    # Show Bio_Poetica poem execution
    print("\n\n🌸 Bio_Poetica Calculator Poem:")
    print("=" * 50)
    
    poem = """when calculation begins:
    add 10 and 20 as first
    multiply first by 2 as doubled
    
The beauty of math
    expressed in verse
        computed naturally"""
    
    print(poem)
    print("\n[This would execute each line as a calculation]")
    print("Result: first = 30, doubled = 60")

if __name__ == "__main__":
    demo()
    
    print("\n\n💡 The Power of KRISPER:")
    print("- Write: 'add 5 and 3 as sum'")
    print("- Get: Executable code that actually adds!")
    print("- No symbols, no syntax, just natural language")