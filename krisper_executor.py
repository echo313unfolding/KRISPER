#!/usr/bin/env python3
"""
KRISPER Executor - Executes KRISPER IR
Turns intermediate representation into real actions
"""

import json
import zlib
import base64
import hashlib
from typing import Dict, Any, Optional

class KrisperExecutor:
    """Execute KRISPER intermediate representation"""
    
    def __init__(self):
        self.variables = {}
        self.operations = {
            'compress': self._op_compress,
            'decompress': self._op_decompress,
            'compare': self._op_compare,
            'hash': self._op_hash,
            'encode': self._op_encode,
            'decode': self._op_decode,
        }
    
    def execute(self, ir: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a KRISPER IR plan"""
        if isinstance(ir, str):
            ir = json.loads(ir)
            
        results = {
            'success': True,
            'outputs': {},
            'log': []
        }
        
        # Execute each operation in the plan
        for op in ir.get('plan', []):
            try:
                result = self._execute_op(op)
                if op.get('out'):
                    self.variables[op['out']] = result
                    results['outputs'][op['out']] = result
                results['log'].append(f"✓ {op['op']} → {op.get('out', 'void')}")
            except Exception as e:
                results['success'] = False
                results['log'].append(f"✗ {op['op']}: {str(e)}")
                break
                
        return results
    
    def _execute_op(self, op: Dict[str, Any]) -> Any:
        """Execute a single operation"""
        op_name = op['op']
        if op_name not in self.operations:
            raise ValueError(f"Unknown operation: {op_name}")
            
        # Resolve inputs
        inputs = self._resolve_inputs(op.get('in', {}))
        params = op.get('params', {})
        
        # Execute operation
        return self.operations[op_name](inputs, params)
    
    def _resolve_inputs(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Resolve variable references in inputs"""
        resolved = {}
        for key, value in inputs.items():
            if isinstance(value, str):
                if value.startswith('utf8:'):
                    # Direct UTF-8 string
                    resolved[key] = value[5:]
                elif value in self.variables:
                    # Variable reference
                    resolved[key] = self.variables[value]
                else:
                    resolved[key] = value
            else:
                resolved[key] = value
        return resolved
    
    def _op_compress(self, inputs: Dict, params: Dict) -> str:
        """Compress data using zlib"""
        data = inputs.get('payload', '')
        if isinstance(data, str):
            data = data.encode('utf-8')
            
        compressed = zlib.compress(data, level=params.get('level', 6))
        return base64.b64encode(compressed).decode('ascii')
    
    def _op_decompress(self, inputs: Dict, params: Dict) -> str:
        """Decompress zlib data"""
        data = inputs.get('data', '')
        compressed = base64.b64decode(data)
        decompressed = zlib.decompress(compressed)
        return decompressed.decode('utf-8')
    
    def _op_compare(self, inputs: Dict, params: Dict) -> bool:
        """Compare two values"""
        a = inputs.get('a', inputs.get('left'))
        b = inputs.get('b', inputs.get('right'))
        return a == b
    
    def _op_hash(self, inputs: Dict, params: Dict) -> str:
        """Hash data using SHA256"""
        data = inputs.get('data', '')
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.sha256(data).hexdigest()
    
    def _op_encode(self, inputs: Dict, params: Dict) -> str:
        """Encode data as base64"""
        data = inputs.get('data', '')
        if isinstance(data, str):
            data = data.encode('utf-8')
        return base64.b64encode(data).decode('ascii')
    
    def _op_decode(self, inputs: Dict, params: Dict) -> str:
        """Decode base64 data"""
        data = inputs.get('data', '')
        decoded = base64.b64decode(data)
        return decoded.decode('utf-8')

def demonstrate_executor():
    """Show the executor in action"""
    print("🚀 KRISPER EXECUTOR DEMO")
    print("=" * 50)
    
    executor = KrisperExecutor()
    
    # Example 1: Simple compression
    ir = {
        "version": "0.1",
        "plan": [
            {
                "op": "compress",
                "in": {"payload": "utf8:Hello, World! This is a test of KRISPER compression."},
                "params": {"level": 9},
                "out": "compressed"
            },
            {
                "op": "hash",
                "in": {"data": "compressed"},
                "out": "checksum"
            },
            {
                "op": "decompress",
                "in": {"data": "compressed"},
                "out": "restored"
            },
            {
                "op": "compare",
                "in": {
                    "left": "utf8:Hello, World! This is a test of KRISPER compression.",
                    "right": "restored"
                },
                "out": "verified"
            }
        ]
    }
    
    print("\n📄 Executing IR:")
    print(json.dumps(ir, indent=2))
    
    results = executor.execute(ir)
    
    print("\n📊 Results:")
    print(f"Success: {results['success']}")
    print("\nLog:")
    for entry in results['log']:
        print(f"  {entry}")
    
    print("\nOutputs:")
    for name, value in results['outputs'].items():
        if isinstance(value, str) and len(value) > 50:
            print(f"  {name}: {value[:50]}...")
        else:
            print(f"  {name}: {value}")

if __name__ == "__main__":
    demonstrate_executor()