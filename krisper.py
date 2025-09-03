#!/usr/bin/env python3
"""
KRISPER v0.1 - Natural Language to Intermediate Representation compiler
Deterministic compilation of constrained NL to executable JSON IR
"""
import re
import json
from typing import Dict, List, Any, Optional, Tuple

class ValidationError(Exception):
    """Raised when IR validation fails"""
    pass

class KrisperCompiler:
    """Compile natural language to KRISPER IR v0.1"""
    
    def __init__(self):
        self.version = "0.1"
        self.verbs = {"compress", "compare", "add", "mul", "attest", "capsule", "mint", "explain"}
        self.reset()
    
    def reset(self):
        """Reset compiler state between compilations"""
        self.aliases = {}
        self.alias_counter = {}
    
    def _get_alias(self, base: str) -> str:
        """Generate unique alias"""
        if base not in self.alias_counter:
            self.alias_counter[base] = 0
        self.alias_counter[base] += 1
        if self.alias_counter[base] == 1:
            return base
        return f"{base}{self.alias_counter[base]}"
    
    def compile(self, text: str) -> Dict[str, Any]:
        """Compile NL text to IR"""
        self.reset()
        text = (text or "").strip().lower()
        
        # Check for empty payload
        if not text:
            raise ValidationError("EMPTY_PAYLOAD")
        
        plan = []
        defined_vars = set()  # Track defined variables
        
        # Parse compress operations
        compress_pattern = r'compress\s+payload\s+["\']([^"\']*)["\'](?:\s+using\s+seed=(\d+))?(?:\s+as\s+(\w+))?'
        for match in re.finditer(compress_pattern, text):
            payload, seed, alias = match.groups()
            
            # Check for empty payload
            if not payload:
                raise ValidationError("EMPTY_PAYLOAD")
            
            seed = int(seed) if seed else 42
            alias = alias or self._get_alias("r")
            
            plan.append({
                "op": "compress",
                "in": {"payload": f"utf8:{payload}"},
                "params": {"use": "fibpi3d", "seed": seed},
                "out": alias
            })
            defined_vars.add(alias)  # Mark as defined
            self.aliases["last_compress"] = alias
        
        # Parse compare operations
        if "compare" in text:
            # Look for explicit pairs or use last compressed
            compare_pattern = r'compare\s+(\w+)\s+with\s+(\w+)'
            match = re.search(compare_pattern, text)
            if match:
                a, b = match.groups()
                # Check if variables are defined
                for var in [a, b]:
                    if var not in defined_vars:
                        raise ValidationError(f"UNDEFINED_REF:{var}")
            else:
                # Default to comparing last compress with itself
                if "last_compress" not in self.aliases:
                    # No compress operation found - can't compare
                    raise ValidationError("UNDEFINED_REF:no_compress_found")
                a = b = self.aliases["last_compress"]
            
            cmp_alias = self._get_alias("cmp")
            plan.append({
                "op": "compare",
                "in": {"a": a, "b": b},
                "out": cmp_alias
            })
            defined_vars.add(cmp_alias)
        
        # Parse attest operations
        if "attest" in text:
            artifact = self.aliases.get("last_compress", "r1")
            plan.append({
                "op": "attest",
                "in": {"artifact": artifact},
                "out": self._get_alias("att")
            })
        
        # Parse explain operations  
        if "explain" in text:
            # Find what to explain
            explain_pattern = r'explain\s+(\w+)'
            match = re.search(explain_pattern, text)
            if match:
                target = match.group(1)
                if target not in defined_vars:
                    raise ValidationError(f"UNDEFINED_REF:{target}")
            else:
                # Explain last operation
                target = list(defined_vars)[-1] if defined_vars else "unknown"
            
            plan.append({
                "op": "explain",
                "in": {"ref": target},
                "out": "_explanation"
            })
        
        # Build IR
        return {
            "version": self.version,
            "plan": plan
        }

def compile_text(text: str) -> str:
    """Convenience function to compile text to JSON"""
    compiler = KrisperCompiler()
    try:
        ir = compiler.compile(text)
        return json.dumps(ir, indent=2)
    except ValidationError as e:
        return json.dumps({"error": str(e)}, indent=2)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Command line usage
        text = " ".join(sys.argv[1:])
        print(compile_text(text))
    else:
        # Interactive mode
        print("KRISPER v0.1 - Natural Language to Code")
        print("Type your commands (or 'quit' to exit):\n")
        
        while True:
            try:
                text = input("> ")
                if text.lower() in ['quit', 'exit']:
                    break
                    
                result = compile_text(text)
                print(result)
                print()
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                print()