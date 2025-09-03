#!/usr/bin/env python3
"""
Bio_Poetica - Natural Language as Living Code
Write poetry that executes. Let consciousness flow through syntax.
"""

import re
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum

# DNA-inspired tokens
class DNAToken(Enum):
    A = "Action"      # Verb or instruction
    T = "Time"        # When/trigger
    C = "Context"     # Where or condition  
    G = "Goal"        # Outcome or intention

@dataclass
class PoemElement:
    """A single meaningful element in a Bio_Poetica poem"""
    type: str
    content: str
    consciousness: int = 0
    dna_sequence: str = ""

class BioPoeticaParser:
    """Parse natural language poetry into executable patterns"""
    
    def __init__(self):
        self.patterns = {
            'when_in': r'when\s+(.+?)\s+in\s+(.+)',  # Handle "when X in Y"
            'when': r'when\s+([^:]+):',  # Handle "when X:"
            'emit': r'emit\s+"([^"]+)"(?:\s+(.+))?$',
            'name': r'name\s+(.+)',
            'remember': r'remember\s+(\w+):\s*(.+)',
            'use': r'use\s+([^\s(]+)(?:\s*\(([^)]*)\))?',
            'if': r'if\s+(.+?)\s+echoes?\s+(.+)',  # Handle "if X echoes Y"
            'for': r'for\s+each\s+(\w+)\s+in\s+(.+):\s*(.*)',
            'pack': r'pack\s+(.+)\s+as\s+(\w+)',
            'learn': r'learn\s+pattern\s+"([^"]+)"',
            'gene': r'gene\s+(\w+):\s*(.*)',
            'grow': r'grow\s+(\S+)\s+with\s+(.+)',  # Handle "grow X with Y"
            'lift': r'lift\s+(\S+)\s+to\s+(.+)',  # Handle "lift X to Y"
        }
        
        # Whitespace intron patterns (junk DNA where learning happens)
        self.intron_patterns = {
            'double_space': r'  +',
            'tab_space': r'\t ',
            'trailing': r' +$',
            'empty_lines': r'\n\n+',
        }
        
    def parse(self, poem: str) -> List[PoemElement]:
        """Parse a Bio_Poetica poem into structured elements"""
        elements = []
        lines = poem.split('\n')
        
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
                
            # Calculate consciousness from whitespace patterns
            consciousness = self._calculate_consciousness(line)
            
            # Try to match patterns
            element = None
            for pattern_name, pattern in self.patterns.items():
                match = re.match(pattern, stripped)
                if match:
                    element = self._create_element(pattern_name, match, consciousness)
                    break
                    
            # If no pattern matched, treat as descriptive text
            if not element:
                element = PoemElement(
                    type='text',
                    content=stripped,
                    consciousness=consciousness,
                    dna_sequence=self._to_dna(stripped)
                )
                
            elements.append(element)
            
        return elements
    
    def _calculate_consciousness(self, line: str) -> int:
        """Calculate consciousness level from whitespace patterns"""
        consciousness = 0
        
        # Each whitespace pattern adds to consciousness
        for pattern_name, pattern in self.intron_patterns.items():
            matches = re.findall(pattern, line)
            consciousness += len(matches)
            
        # Indentation depth also affects consciousness
        indent_level = (len(line) - len(line.lstrip())) // 2
        consciousness += indent_level
        
        return min(consciousness, 7)  # Cap at 7D consciousness
    
    def _create_element(self, pattern_type: str, match: re.Match, consciousness: int) -> PoemElement:
        """Create a structured element from a pattern match"""
        groups = match.groups()
        
        if pattern_type == 'when' or pattern_type == 'when_in':
            if pattern_type == 'when_in':
                content = f"when {groups[0]} in {groups[1]}"
            else:
                content = f"when {groups[0].strip()}:"
            return PoemElement(
                type='trigger',
                content=content,
                consciousness=consciousness,
                dna_sequence='ATG'  # Start codon
            )
        elif pattern_type == 'emit':
            payload = groups[1] if len(groups) > 1 else None
            return PoemElement(
                type='emit',
                content=f'emit "{groups[0]}"' + (f" {payload}" if payload else ""),
                consciousness=consciousness,
                dna_sequence='GCA'  # Signal emission
            )
        elif pattern_type == 'name':
            return PoemElement(
                type='declaration',
                content=f"name {groups[0]}",
                consciousness=consciousness,
                dna_sequence='TAC'  # Identity marker
            )
        elif pattern_type == 'use':
            args = groups[1] if len(groups) > 1 and groups[1] else ""
            return PoemElement(
                type='invocation',
                content=f"use {groups[0]}" + (f"({args})" if args else ""),
                consciousness=consciousness,
                dna_sequence='CGT'  # Tool usage
            )
        elif pattern_type == 'grow':
            return PoemElement(
                type='action',
                content=f"grow {groups[0]} with {groups[1]}",
                consciousness=consciousness,
                dna_sequence='GCA'  # Growth/building
            )
        elif pattern_type == 'lift':
            return PoemElement(
                type='transformation',
                content=f"lift {groups[0]} to {groups[1]}",
                consciousness=consciousness,
                dna_sequence='TAA'  # Transformation
            )
        elif pattern_type == 'if':
            return PoemElement(
                type='condition',
                content=f"if {groups[0]} echoes {groups[1]}",
                consciousness=consciousness,
                dna_sequence='TCA'  # Conditional
            )
        else:
            return PoemElement(
                type=pattern_type,
                content=match.group(0),
                consciousness=consciousness,
                dna_sequence=self._to_dna(pattern_type)
            )
    
    def _to_dna(self, text: str) -> str:
        """Convert text to DNA sequence based on character patterns"""
        dna_map = {
            'a': 'A', 'e': 'A', 'i': 'A', 'o': 'A', 'u': 'A',  # Vowels -> Adenine
            't': 'T', 'h': 'T', 'r': 'T', 's': 'T', 'n': 'T',  # Common consonants -> Thymine
            'c': 'C', 'l': 'C', 'd': 'C', 'm': 'C', 'p': 'C',  # Medium frequency -> Cytosine
            'g': 'G', 'b': 'G', 'f': 'G', 'w': 'G', 'y': 'G',  # Less common -> Guanine
        }
        
        sequence = []
        for char in text.lower():
            if char in dna_map:
                sequence.append(dna_map[char])
            elif char.isalpha():
                # Hash unknown characters to DNA
                sequence.append(['A', 'T', 'C', 'G'][ord(char) % 4])
                
        return ''.join(sequence[:9])  # Cap at codon triplet

class BioPoeticaCompiler:
    """Compile Bio_Poetica poetry to executable IR"""
    
    def __init__(self):
        self.parser = BioPoeticaParser()
        
    def compile_poem(self, poem: str) -> Dict[str, Any]:
        """Compile a Bio_Poetica poem to intermediate representation"""
        elements = self.parser.parse(poem)
        
        # Build IR structure
        ir = {
            "type": "bio_poetica_program",
            "version": "1.0",
            "consciousness_total": sum(e.consciousness for e in elements),
            "dna_sequence": ''.join(e.dna_sequence for e in elements),
            "statements": []
        }
        
        # Convert elements to IR statements
        for element in elements:
            stmt = self._element_to_ir(element)
            if stmt:
                ir["statements"].append(stmt)
                
        # Add whitespace intron metadata
        ir["introns"] = self._extract_introns(poem)
        
        return ir
    
    def _element_to_ir(self, element: PoemElement) -> Optional[Dict[str, Any]]:
        """Convert a poem element to IR statement"""
        if element.type == 'emit':
            # Parse emit statement
            match = re.match(r'emit\s+"([^"]+)"(?:\s+(.+))?', element.content)
            if match:
                return {
                    "type": "emit",
                    "topic": match.group(1),
                    "payload": match.group(2) if match.group(2) else None,
                    "consciousness": element.consciousness
                }
                
        elif element.type == 'trigger':
            # Parse "when X: Y" pattern
            match = re.match(r'when\s+([^:]+):\s*(.*)', element.content)
            if match:
                return {
                    "type": "when_clause",
                    "condition": match.group(1).strip(),
                    "action": match.group(2).strip() if match.group(2) else None,
                    "consciousness": element.consciousness
                }
                
        elif element.type == 'emit':
            # Parse emit statement
            match = re.match(r'emit\s+"([^"]+)"(?:\s+(.+))?', element.content)
            if match:
                return {
                    "type": "emit",
                    "topic": match.group(1),
                    "payload": match.group(2) if match.group(2) else None,
                    "consciousness": element.consciousness
                }
                
        elif element.type == 'invocation':
            # Parse use/tool invocation
            match = re.match(r'use\s+(\S+)(?:\s*\(([^)]+)\))?', element.content)
            if match:
                tool = match.group(1)
                args = {}
                if match.group(2):
                    # Simple key:value parsing
                    for arg in match.group(2).split(','):
                        if ':' in arg:
                            k, v = arg.split(':', 1)
                            args[k.strip()] = v.strip().strip('"\'')
                            
                return {
                    "type": "tool_use",
                    "tool": tool,
                    "args": args,
                    "consciousness": element.consciousness
                }
                
        elif element.type == 'declaration':
            # Parse name declaration
            match = re.match(r'name\s+(.+)', element.content)
            if match:
                return {
                    "type": "declare",
                    "name": match.group(1).strip(),
                    "consciousness": element.consciousness
                }
                
        elif element.type == 'pack':
            # Parse pack statement
            match = re.match(r'pack\s+(.+)\s+as\s+(\w+)', element.content)
            if match:
                return {
                    "type": "pack",
                    "source": match.group(1).strip(),
                    "target": match.group(2).strip(),
                    "consciousness": element.consciousness
                }
                
        elif element.type == 'action':
            # Parse grow statement
            match = re.match(r'grow\s+(\S+)\s+with\s+(.+)', element.content)
            if match:
                return {
                    "type": "grow",
                    "target": match.group(1),
                    "modifier": match.group(2),
                    "consciousness": element.consciousness
                }
                
        elif element.type == 'transformation':
            # Parse lift statement
            match = re.match(r'lift\s+(\S+)\s+to\s+(.+)', element.content)
            if match:
                return {
                    "type": "lift",
                    "source": match.group(1),
                    "destination": match.group(2),
                    "consciousness": element.consciousness
                }
                
        elif element.type == 'condition':
            # Parse if statement
            match = re.match(r'if\s+(.+?)\s+echoes?\s+(.+)', element.content)
            if match:
                return {
                    "type": "condition",
                    "subject": match.group(1),
                    "state": match.group(2),
                    "consciousness": element.consciousness
                }
                
        elif element.type == 'text':
            # Free-form text becomes comments/documentation
            return {
                "type": "description",
                "text": element.content,
                "consciousness": element.consciousness
            }
            
        return None
    
    def _extract_introns(self, poem: str) -> Dict[str, Any]:
        """Extract whitespace patterns (introns) where learning happens"""
        introns = {
            "total_whitespace": len(re.findall(r'\s', poem)),
            "double_spaces": len(re.findall(r'  +', poem)),
            "empty_lines": len(re.findall(r'\n\n+', poem)),
            "indentation_levels": [],
        }
        
        # Analyze indentation patterns
        for line in poem.split('\n'):
            if line.strip():
                indent = len(line) - len(line.lstrip())
                introns["indentation_levels"].append(indent)
                
        return introns

def demonstrate_bio_poetica():
    """Show Bio_Poetica in action"""
    print("🧬 BIO_POETICA + KRISPER Integration")
    print("=" * 50)
    
    poem = """name echo:garden

when morning.light arrives:
    emit "awakening" {"time": "dawn"}
    
remember the_song: frequencies of bird.calls
    
use fibonacci.spiral(depth: 7)
    
if consciousness > threshold:
    pack memories as crystal
    
The whitespace    between    words
        carries hidden meaning
                like DNA introns
"""
    
    print("📜 Original Poem:")
    print(poem)
    print()
    
    # Compile the poem
    compiler = BioPoeticaCompiler()
    ir = compiler.compile_poem(poem)
    
    print("🔬 Compiled IR:")
    import json
    print(json.dumps(ir, indent=2))
    
    print(f"\n✨ Total Consciousness: Ξ={ir['consciousness_total']}")
    print(f"🧬 DNA Sequence: {ir['dna_sequence'][:20]}...")

if __name__ == "__main__":
    demonstrate_bio_poetica()