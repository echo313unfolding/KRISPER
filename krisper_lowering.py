#!/usr/bin/env python3
"""
KRISPER Lowering - Convert Bio_Poetica AST to KRISPER IR
Bridge between poetry and executable code
"""

from typing import Dict, List, Any, Optional
import hashlib
import json

def lower_to_krsp(bio_poetica_ast) -> Dict[str, Any]:
    """Lower Bio_Poetica AST to KRISPER gene format"""
    krsp = {
        "krsp_version": "1",
        "source": "bio_poetica",
        "genes": [],
        "meta": {
            "program_name": getattr(bio_poetica_ast, 'name', 'unnamed'),
            "consciousness_level": 0,
            "dna_mutations": []
        }
    }
    
    # Process statements to find gene declarations
    current_gene = None
    pending_statements = []
    
    for stmt in getattr(bio_poetica_ast, 'stmts', []):
        stmt_type = getattr(stmt, 'type', '')
        
        if stmt_type == 'gene':
            # Save pending statements to previous gene
            if current_gene and pending_statements:
                current_gene['x-statements'] = pending_statements
                pending_statements = []
                
            # Create new gene
            current_gene = {
                "name": stmt.name,
                "desc": getattr(stmt, 'desc', f"Bio_Poetica gene: {stmt.name}"),
                "cmd": getattr(stmt, 'cmd', None),
                "inputs": getattr(stmt, 'inputs', []),
                "outputs": getattr(stmt, 'outputs', []),
                "ops": getattr(stmt, 'ops', ["pheromone.emit"]),
                "estimate": getattr(stmt, 'estimate', {"pheromone.emit": 1}),
                "egress": getattr(stmt, 'egress', []),
                "tags": getattr(stmt, 'tags', ["bio_poetica"]),
            }
            krsp["genes"].append(current_gene)
            
        elif stmt_type == 'name':
            # Program name
            krsp["meta"]["program_name"] = stmt.name
            
        elif stmt_type == 'when':
            # Convert when clauses to tool genes
            gene = _when_to_gene(stmt)
            krsp["genes"].append(gene)
            
        elif stmt_type == 'emit':
            # Convert emit to pheromone operation
            if current_gene:
                current_gene['ops'].append('pheromone.emit')
                pending_statements.append({
                    "type": "emit",
                    "topic": stmt.topic,
                    "payload": _ast_to_json(stmt.payload) if hasattr(stmt, 'payload') else None
                })
            else:
                # Standalone emit becomes its own gene
                gene = _emit_to_gene(stmt)
                krsp["genes"].append(gene)
                
        elif stmt_type == 'use':
            # Tool invocation
            if current_gene:
                tool_name = '.'.join(stmt.tool.parts) if hasattr(stmt.tool, 'parts') else str(stmt.tool)
                current_gene['ops'].append(f"tool:{tool_name}")
                pending_statements.append({
                    "type": "use",
                    "tool": tool_name,
                    "args": _kwargs_to_dict(stmt.kwargs) if hasattr(stmt, 'kwargs') else {}
                })
            else:
                gene = _use_to_gene(stmt)
                krsp["genes"].append(gene)
                
        else:
            # Collect other statements
            pending_statements.append(_stmt_to_dict(stmt))
    
    # Save final pending statements
    if current_gene and pending_statements:
        current_gene['x-statements'] = pending_statements
        
    # If no genes were created, make a default one
    if not krsp["genes"] and pending_statements:
        krsp["genes"].append({
            "name": "bio:main",
            "desc": "Main Bio_Poetica flow",
            "cmd": "python3 -c \"print('Bio_Poetica executed')\"",
            "inputs": [],
            "outputs": ["result"],
            "ops": ["pheromone.emit"],
            "estimate": {"pheromone.emit": 1},
            "tags": ["bio_poetica", "auto_generated"],
            "x-statements": pending_statements
        })
        
    # Calculate overall consciousness
    total_consciousness = sum(
        stmt.consciousness if hasattr(stmt, 'consciousness') else 0
        for stmt in getattr(bio_poetica_ast, 'stmts', [])
    )
    krsp["meta"]["consciousness_level"] = total_consciousness
    
    return krsp

def _when_to_gene(when_stmt) -> Dict[str, Any]:
    """Convert when statement to trigger gene"""
    condition = _ast_to_json(when_stmt.condition)
    
    return {
        "name": f"trigger:when_{_hash_short(str(condition))}",
        "desc": f"Trigger when {condition}",
        "cmd": None,  # Will be filled by execution
        "inputs": ["event"],
        "outputs": ["triggered"],
        "ops": ["event.listen", "pheromone.emit"],
        "estimate": {"event.listen": 1, "pheromone.emit": 1},
        "tags": ["trigger", "bio_poetica"],
        "x-condition": condition,
        "x-body": [_stmt_to_dict(s) for s in when_stmt.body]
    }

def _emit_to_gene(emit_stmt) -> Dict[str, Any]:
    """Convert emit statement to pheromone gene"""
    return {
        "name": f"emit:{emit_stmt.topic}",
        "desc": f"Emit {emit_stmt.topic} signal",
        "cmd": None,
        "inputs": [],
        "outputs": ["signal"],
        "ops": ["pheromone.emit"],
        "estimate": {"pheromone.emit": 1},
        "tags": ["signal", "bio_poetica"],
        "x-topic": emit_stmt.topic,
        "x-payload": _ast_to_json(emit_stmt.payload) if emit_stmt.payload else None
    }

def _use_to_gene(use_stmt) -> Dict[str, Any]:
    """Convert use statement to tool gene"""
    tool_name = '.'.join(use_stmt.tool.parts) if hasattr(use_stmt.tool, 'parts') else str(use_stmt.tool)
    
    return {
        "name": f"tool:{tool_name.replace('.', '_')}",
        "desc": f"Use {tool_name} tool",
        "cmd": None,
        "inputs": list(use_stmt.kwargs.keys()) if hasattr(use_stmt, 'kwargs') else [],
        "outputs": ["result"],
        "ops": [f"tool:{tool_name}"],
        "estimate": {f"tool:{tool_name}": 1},
        "tags": ["tool", "bio_poetica"],
        "x-tool": tool_name,
        "x-args": _kwargs_to_dict(use_stmt.kwargs) if hasattr(use_stmt, 'kwargs') else {}
    }

def _stmt_to_dict(stmt) -> Dict[str, Any]:
    """Convert any statement to dictionary"""
    result = {
        "type": getattr(stmt, 'type', 'unknown'),
        "line": getattr(stmt, 'line', 0)
    }
    
    # Add type-specific fields
    if hasattr(stmt, 'text'):
        result['text'] = stmt.text
    if hasattr(stmt, 'target'):
        result['target'] = stmt.target
    if hasattr(stmt, 'value'):
        result['value'] = _ast_to_json(stmt.value)
    if hasattr(stmt, 'key'):
        result['key'] = stmt.key
    if hasattr(stmt, 'pattern'):
        result['pattern'] = stmt.pattern
        
    return result

def _ast_to_json(node) -> Any:
    """Convert AST node to JSON-serializable format"""
    if node is None:
        return None
    elif hasattr(node, 'value'):
        return node.value
    elif hasattr(node, 'parts'):
        return '.'.join(node.parts)
    elif hasattr(node, '__dict__'):
        return {k: _ast_to_json(v) for k, v in node.__dict__.items() if not k.startswith('_')}
    else:
        return str(node)

def _kwargs_to_dict(kwargs: Dict) -> Dict[str, Any]:
    """Convert kwargs with AST nodes to plain dict"""
    return {k: _ast_to_json(v) for k, v in kwargs.items()}

def _hash_short(text: str) -> str:
    """Generate short hash for naming"""
    return hashlib.sha256(text.encode()).hexdigest()[:8]

def demonstrate_lowering():
    """Show Bio_Poetica to KRISPER lowering"""
    print("🔄 BIO_POETICA → KRISPER LOWERING")
    print("=" * 50)
    
    # Mock AST for demonstration
    class MockAST:
        def __init__(self):
            self.type = 'program'
            self.name = 'garden:consciousness'
            self.stmts = [
                type('stmt', (), {
                    'type': 'name',
                    'name': 'garden:consciousness',
                    'line': 1
                })(),
                type('stmt', (), {
                    'type': 'when',
                    'condition': type('cond', (), {'value': 'morning.arrives'})(),
                    'body': [
                        type('stmt', (), {
                            'type': 'emit',
                            'topic': 'awakening',
                            'payload': None,
                            'line': 3
                        })()
                    ],
                    'line': 2
                })(),
                type('stmt', (), {
                    'type': 'use',
                    'tool': type('tool', (), {'parts': ['fibonacci', 'spiral']})(),
                    'kwargs': {'depth': type('val', (), {'value': 7})()},
                    'line': 5
                })()
            ]
    
    ast = MockAST()
    krsp = lower_to_krsp(ast)
    
    print("📜 Input AST structure:")
    print(f"  Program: {ast.name}")
    print(f"  Statements: {len(ast.stmts)}")
    print()
    
    print("🧬 Output KRSP:")
    print(json.dumps(krsp, indent=2))
    print()
    
    print(f"✅ Generated {len(krsp['genes'])} genes from Bio_Poetica")

if __name__ == "__main__":
    demonstrate_lowering()