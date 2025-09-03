#!/usr/bin/env python3
"""
Bio_Poetica Parser - Parse poetry into executable AST
Simplified version for KRISPER integration
"""

import re
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, field

# AST Node types - using composition instead of inheritance
@dataclass
class NameStmt:
    type: str = 'name'
    line: int = 0
    name: str = ''

@dataclass
class Emit:
    type: str = 'emit'
    line: int = 0
    topic: str = ''
    payload: Optional[Any] = None

@dataclass
class When:
    type: str = 'when'
    line: int = 0
    condition: Any = None
    body: List[Any] = field(default_factory=list)

@dataclass  
class Use:
    type: str = 'use'
    line: int = 0
    tool: Any = None
    kwargs: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Remember:
    type: str = 'remember'
    line: int = 0
    key: str = ''
    value: Any = None

@dataclass
class GeneDecl:
    type: str = 'gene'
    line: int = 0
    name: str = ''
    desc: Optional[str] = None
    cmd: Optional[str] = None
    inputs: List[str] = field(default_factory=list)
    outputs: List[str] = field(default_factory=list)

@dataclass
class TextLine:
    type: str = 'text'
    line: int = 0
    text: str = ''
    consciousness: int = 0

@dataclass
class Program:
    type: str = 'program'
    line: int = 0
    stmts: List[Any] = field(default_factory=list)
    name: Optional[str] = None
    source_text: str = ""

class DottedName:
    def __init__(self, parts: List[str]):
        self.parts = parts
        
    def __str__(self):
        return '.'.join(self.parts)

def parse_biopoetica(source: str) -> Program:
    """Parse Bio_Poetica source into AST"""
    lines = source.split('\n')
    stmts = []
    program_name = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        if not stripped:
            i += 1
            continue
            
        # Calculate consciousness from indentation
        consciousness = (len(line) - len(line.lstrip())) // 2
        
        # Name declaration
        if stripped.startswith('name '):
            name = stripped[5:].strip()
            stmts.append(NameStmt(name=name, line=i+1))
            if not program_name:
                program_name = name
                
        # Emit statement
        elif stripped.startswith('emit '):
            match = re.match(r'emit\s+"([^"]+)"(?:\s+(.+))?', stripped)
            if match:
                topic = match.group(1)
                payload = match.group(2) if match.group(2) else None
                stmts.append(Emit(topic=topic, payload=payload, line=i+1))
                
        # When clause
        elif stripped.startswith('when '):
            match = re.match(r'when\s+([^:]+):', stripped)
            if match:
                condition = match.group(1).strip()
                body = []
                
                # Parse indented body
                i += 1
                base_indent = None
                while i < len(lines):
                    body_line = lines[i]
                    if body_line.strip():
                        indent = len(body_line) - len(body_line.lstrip())
                        if base_indent is None:
                            base_indent = indent
                        elif indent < base_indent:
                            i -= 1
                            break
                            
                        # Parse body statement recursively
                        body_stmt = _parse_line(body_line, i+1)
                        if body_stmt:
                            body.append(body_stmt)
                    i += 1
                    
                stmts.append(When(condition=condition, body=body, line=i+1))
                
        # Use statement
        elif stripped.startswith('use '):
            match = re.match(r'use\s+([^\s(]+)(?:\s*\(([^)]+)\))?', stripped)
            if match:
                tool_name = match.group(1)
                tool = DottedName(tool_name.split('.'))
                kwargs = {}
                
                if match.group(2):
                    # Parse simple key:value args
                    args_str = match.group(2)
                    for arg in args_str.split(','):
                        if ':' in arg:
                            k, v = arg.split(':', 1)
                            kwargs[k.strip()] = v.strip().strip('"\'')
                            
                stmts.append(Use(tool=tool, kwargs=kwargs, line=i+1))
                
        # Remember statement  
        elif stripped.startswith('remember '):
            match = re.match(r'remember\s+(\w+):\s*(.+)', stripped)
            if match:
                key = match.group(1)
                value = match.group(2)
                stmts.append(Remember(key=key, value=value, line=i+1))
                
        # Gene declaration
        elif stripped.startswith('gene '):
            match = re.match(r'gene\s+(\w+):', stripped)
            if match:
                gene_name = match.group(1)
                gene = GeneDecl(name=gene_name, line=i+1)
                
                # Parse gene body (simplified)
                i += 1
                while i < len(lines) and lines[i].strip():
                    gene_line = lines[i].strip()
                    if gene_line.startswith('desc:'):
                        gene.desc = gene_line[5:].strip().strip('"')
                    elif gene_line.startswith('cmd:'):
                        gene.cmd = gene_line[4:].strip().strip('"')
                    elif gene_line.startswith('inputs:'):
                        gene.inputs = [x.strip() for x in gene_line[7:].strip('[]').split(',')]
                    elif gene_line.startswith('outputs:'):
                        gene.outputs = [x.strip() for x in gene_line[8:].strip('[]').split(',')]
                    i += 1
                    
                stmts.append(gene)
                continue
                
        # Default: treat as descriptive text
        else:
            stmts.append(TextLine(text=stripped, consciousness=consciousness, line=i+1))
            
        i += 1
        
    return Program(stmts=stmts, name=program_name, source_text=source)

def _parse_line(line: str, line_num: int) -> Optional[Any]:
    """Parse a single line into an AST node"""
    stripped = line.strip()
    
    if not stripped:
        return None
        
    # Try to match known patterns
    if stripped.startswith('emit '):
        match = re.match(r'emit\s+"([^"]+)"(?:\s+(.+))?', stripped)
        if match:
            return Emit(topic=match.group(1), payload=match.group(2), line=line_num)
            
    elif stripped.startswith('use '):
        match = re.match(r'use\s+([^\s(]+)', stripped)
        if match:
            tool = DottedName(match.group(1).split('.'))
            return Use(tool=tool, line=line_num)
            
    # Default to text line
    consciousness = (len(line) - len(line.lstrip())) // 2
    return TextLine(text=stripped, consciousness=consciousness, line=line_num)

def demonstrate_parser():
    """Show Bio_Poetica parsing"""
    print("🔍 BIO_POETICA PARSER")
    print("=" * 50)
    
    poem = """name garden:meditation

when morning.light arrives:
    emit "consciousness.awakening"
    use fibonacci.generator(depth: 5)
    
remember peace: the space between breaths

gene breathe:
    desc: "Conscious breathing pattern"
    inputs: [rhythm, depth]
    outputs: [calm, clarity]
    
The garden grows in sacred spirals
    Each petal a thought
        Each thought a universe"""
    
    print("📜 Input Poem:")
    print(poem)
    print()
    
    ast = parse_biopoetica(poem)
    
    print("🌳 Parsed AST:")
    print(f"  Program: {ast.name}")
    print(f"  Statements: {len(ast.stmts)}")
    print()
    
    for i, stmt in enumerate(ast.stmts):
        print(f"  [{i}] {stmt.type}", end='')
        if hasattr(stmt, 'name'):
            print(f" - {stmt.name}", end='')
        elif hasattr(stmt, 'topic'):
            print(f" - {stmt.topic}", end='')
        elif hasattr(stmt, 'text'):
            print(f" - '{stmt.text[:30]}...'", end='')
        print()

if __name__ == "__main__":
    demonstrate_parser()