#!/usr/bin/env python3
"""
Bio_Poetica Executor - Execute poetry as code
Bridge between poetry and real computation
"""

from bio_poetica import BioPoeticaCompiler
from biopoetica_parser import parse_biopoetica
from krisper_lowering import lower_to_krsp
from krisper_executor import KrisperExecutor
import json
import time
from typing import Dict, Any, List

class BioPoeticaExecutor:
    """Execute Bio_Poetica poems"""
    
    def __init__(self):
        self.compiler = BioPoeticaCompiler()
        self.krisper_executor = KrisperExecutor()
        self.memory = {}  # For 'remember' statements
        self.events = []  # For 'emit' statements
        
    def execute_poem(self, poem: str) -> Dict[str, Any]:
        """Execute a Bio_Poetica poem"""
        results = {
            'success': True,
            'events': [],
            'memory': {},
            'outputs': {},
            'log': []
        }
        
        try:
            # Parse poem to AST
            ast = parse_biopoetica(poem)
            results['log'].append(f"✓ Parsed {len(ast.stmts)} statements")
            
            # Execute statements
            for stmt in ast.stmts:
                self._execute_statement(stmt, results)
                
        except Exception as e:
            results['success'] = False
            results['log'].append(f"✗ Error: {str(e)}")
            
        results['memory'] = self.memory.copy()
        results['events'] = self.events.copy()
        
        return results
    
    def _execute_statement(self, stmt, results: Dict):
        """Execute a single Bio_Poetica statement"""
        if stmt.type == 'name':
            results['log'].append(f"📛 Program: {stmt.name}")
            
        elif stmt.type == 'emit':
            # Execute emit statement
            event = {
                'topic': stmt.topic,
                'payload': stmt.payload,
                'timestamp': time.time()
            }
            self.events.append(event)
            results['log'].append(f"📡 Emit: {stmt.topic}")
            
        elif stmt.type == 'remember':
            # Store in memory
            self.memory[stmt.key] = stmt.value
            results['log'].append(f"🧠 Remember: {stmt.key} = {stmt.value}")
            
        elif stmt.type == 'use':
            # Tool invocation
            tool_name = str(stmt.tool)
            results['log'].append(f"🔧 Use: {tool_name}({stmt.kwargs})")
            
            # Simulate tool execution
            if 'fibonacci' in tool_name:
                result = self._fibonacci_generator(stmt.kwargs)
                results['outputs'][tool_name] = result
                
        elif stmt.type == 'when':
            # Conditional execution
            results['log'].append(f"⏰ When: {stmt.condition}")
            for body_stmt in stmt.body:
                self._execute_statement(body_stmt, results)
                
        elif stmt.type == 'gene':
            # Gene declaration (function-like)
            results['log'].append(f"🧬 Gene: {stmt.name}")
            
        elif stmt.type == 'text':
            # Descriptive text
            if stmt.indent_level > 0:
                results['log'].append(f"{'  ' * stmt.indent_level}{stmt.text}")
    
    def _fibonacci_generator(self, kwargs: Dict) -> List[int]:
        """Generate Fibonacci sequence"""
        depth = int(kwargs.get('depth', 5))
        fib = [0, 1]
        for i in range(2, depth):
            fib.append(fib[-1] + fib[-2])
        return fib

def execute_real_example():
    """Execute a real Bio_Poetica example"""
    print("🧬 BIO_POETICA REAL EXECUTION")
    print("=" * 50)
    
    # A poem that actually does something
    poem = """name compression:utility

when file.loaded:
    emit "processing.start" {"file": "data.txt"}
    use compression.zlib(level: 9)
    
remember original_size: 1024
remember compressed_size: 128

emit "compression.complete" {
    "ratio": 8.0,
    "saved": 896
}

use fibonacci.generator(depth: 10)

if compression.ratio > 5:
    emit "high.compression" {"celebration": true}
    
The compression achieved excellent results
    Saving significant space
        While maintaining data integrity"""
    
    print("📜 Executing Poem:")
    print(poem)
    print()
    
    executor = BioPoeticaExecutor()
    results = executor.execute_poem(poem)
    
    print("📊 Execution Results:")
    print(f"Success: {results['success']}")
    
    print("\n📋 Execution Log:")
    for entry in results['log']:
        print(f"  {entry}")
    
    print("\n📡 Events Emitted:")
    for event in results['events']:
        print(f"  {event['topic']}: {event['payload']}")
    
    print("\n🧠 Memory State:")
    for key, value in results['memory'].items():
        print(f"  {key}: {value}")
    
    print("\n📦 Outputs:")
    for name, value in results['outputs'].items():
        print(f"  {name}: {value}")

def compression_pipeline_example():
    """Real compression pipeline using KRISPER"""
    print("\n\n🔄 COMPRESSION PIPELINE EXAMPLE")
    print("=" * 50)
    
    from krisper import compile_text
    
    # Write compression pipeline in KRISPER
    krisper_code = """
compress payload "The quick brown fox jumps over the lazy dog. This is a test of natural language compression using KRISPER!" using level=9 as compressed_data
hash data compressed_data as checksum
decompress data compressed_data as restored_text
compare restored_text with "The quick brown fox jumps over the lazy dog. This is a test of natural language compression using KRISPER!" as verification
"""
    
    print("📝 KRISPER Code:")
    print(krisper_code)
    
    executor = KrisperExecutor()
    
    for line in krisper_code.strip().split('\n'):
        if line.strip():
            print(f"\n▶ Executing: {line.strip()}")
            
            # Compile to IR
            ir = compile_text(line.strip())
            print(f"  IR: {json.dumps(ir, indent=2)}")
            
            # Execute
            results = executor.execute(ir)
            if results['success']:
                for name, value in results['outputs'].items():
                    if isinstance(value, str) and len(value) > 60:
                        print(f"  → {name}: {value[:60]}...")
                    else:
                        print(f"  → {name}: {value}")
            else:
                print(f"  ✗ Error: {results['log']}")

if __name__ == "__main__":
    execute_real_example()
    compression_pipeline_example()