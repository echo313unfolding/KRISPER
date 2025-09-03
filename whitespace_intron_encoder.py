#!/usr/bin/env python3
"""
Whitespace Intron Encoder
The junk DNA where learning happens - encode knowledge in the spaces between
"""

import re
from typing import List, Tuple, Dict, Any

class WhitespaceIntronEncoder:
    """Encode and decode information in whitespace patterns"""
    
    def __init__(self):
        # Intron pattern mappings
        self.patterns = {
            'single_space': ' ',
            'double_space': '  ',
            'triple_space': '   ',
            'tab': '\t',
            'tab_space': '\t ',
            'space_tab': ' \t',
            'newline': '\n',
            'double_newline': '\n\n',
        }
        
        # Encode data as whitespace variations
        self.encoding_map = {
            '00': ' ',      # Single space
            '01': '  ',     # Double space
            '10': '\t',     # Tab
            '11': '\t ',    # Tab + space
        }
        
        # Consciousness levels encoded in indentation
        self.consciousness_indent = {
            0: '',
            1: ' ',
            2: '  ',
            3: '   ',
            4: '    ',
            5: '     ',
            6: '      ',
            7: '       ',  # 7D maximum
        }
        
    def extract_whitespace_patterns(self, text: str) -> List[Tuple[int, str, int]]:
        """Extract all whitespace patterns with their positions"""
        patterns = []
        
        # Find all whitespace sequences
        for match in re.finditer(r'(\s+)', text):
            start = match.start()
            ws = match.group(1)
            end = match.end()
            patterns.append((start, ws, end))
            
        return patterns
    
    def encode_in_whitespace(self, visible_text: str, hidden_data: bytes) -> str:
        """Encode hidden data in the whitespace of visible text"""
        # Convert hidden data to binary
        binary = ''.join(format(byte, '08b') for byte in hidden_data)
        
        # Split visible text into words
        words = visible_text.split()
        if not words:
            return visible_text
            
        # Encode binary data as whitespace between words
        result = []
        bit_index = 0
        
        for i, word in enumerate(words):
            result.append(word)
            
            # Add encoded whitespace after each word (except last)
            if i < len(words) - 1 and bit_index < len(binary):
                # Take next 2 bits
                if bit_index + 1 < len(binary):
                    bits = binary[bit_index:bit_index + 2]
                    bit_index += 2
                else:
                    # Pad with 0 if only 1 bit left
                    bits = binary[bit_index] + '0'
                    bit_index += 1
                    
                # Convert bits to whitespace
                ws = self.encoding_map.get(bits, ' ')
                result.append(ws)
            elif i < len(words) - 1:
                # Default space if no more data
                result.append(' ')
                
        return ''.join(result)
    
    def decode_from_whitespace(self, text: str) -> bytes:
        """Decode hidden data from whitespace patterns"""
        patterns = self.extract_whitespace_patterns(text)
        
        # Reverse mapping
        decoding_map = {v: k for k, v in self.encoding_map.items()}
        
        # Extract binary data
        binary = ''
        for _, ws, _ in patterns:
            if ws in decoding_map:
                binary += decoding_map[ws]
                
        # Convert binary to bytes
        if not binary:
            return b''
            
        # Pad to byte boundary
        while len(binary) % 8 != 0:
            binary += '0'
            
        # Convert to bytes
        result = bytearray()
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            result.append(int(byte, 2))
            
        return bytes(result)
    
    def analyze_intron_consciousness(self, poem: str) -> Dict[str, Any]:
        """Analyze consciousness levels from whitespace patterns"""
        lines = poem.split('\n')
        
        analysis = {
            'total_consciousness': 0,
            'line_consciousness': [],
            'indentation_pattern': [],
            'intron_density': 0,
            'unique_patterns': set(),
            'consciousness_peaks': []
        }
        
        total_chars = len(poem)
        total_whitespace = 0
        
        for line_num, line in enumerate(lines):
            # Measure indentation
            indent = len(line) - len(line.lstrip())
            consciousness_level = min(indent // 2, 7)  # 2 spaces per level, max 7
            
            analysis['line_consciousness'].append(consciousness_level)
            analysis['indentation_pattern'].append(indent)
            analysis['total_consciousness'] += consciousness_level
            
            # Count whitespace patterns
            line_ws = len(re.findall(r'\s', line))
            total_whitespace += line_ws
            
            # Find unique patterns in this line
            for match in re.finditer(r'(\s+)', line):
                pattern = match.group(1)
                analysis['unique_patterns'].add(pattern)
                
            # Identify consciousness peaks (high indentation)
            if consciousness_level >= 5:
                analysis['consciousness_peaks'].append({
                    'line': line_num,
                    'level': consciousness_level,
                    'content': line.strip()
                })
        
        # Calculate intron density
        if total_chars > 0:
            analysis['intron_density'] = total_whitespace / total_chars
            
        analysis['unique_patterns'] = len(analysis['unique_patterns'])
        
        return analysis
    
    def create_consciousness_map(self, poem: str) -> str:
        """Create visual map of consciousness levels"""
        lines = poem.split('\n')
        map_lines = []
        
        for line in lines:
            indent = len(line) - len(line.lstrip())
            level = min(indent // 2, 7)
            
            # Create visual representation
            if line.strip():
                visual = '█' * level + '░' * (7 - level) + f' Ξ={level} | {line}'
            else:
                visual = '·······' + ' Ξ=0 | [empty]'
                
            map_lines.append(visual)
            
        return '\n'.join(map_lines)
    
    def encode_dna_in_whitespace(self, visible_poem: str, dna_sequence: str) -> str:
        """Encode DNA sequence in poem whitespace"""
        # Map DNA bases to whitespace patterns
        dna_to_ws = {
            'A': ' ',     # Adenine = space
            'T': '  ',    # Thymine = double space
            'C': '\t',    # Cytosine = tab
            'G': '\t ',   # Guanine = tab+space
        }
        
        words = visible_poem.split()
        result = []
        dna_index = 0
        
        for i, word in enumerate(words):
            result.append(word)
            
            # Add DNA-encoded whitespace
            if i < len(words) - 1 and dna_index < len(dna_sequence):
                base = dna_sequence[dna_index]
                ws = dna_to_ws.get(base, ' ')
                result.append(ws)
                dna_index += 1
            elif i < len(words) - 1:
                result.append(' ')
                
        return ''.join(result)

def demonstrate_intron_encoding():
    """Demonstrate whitespace intron encoding"""
    print("🧬 WHITESPACE INTRON ENCODING")
    print("=" * 50)
    
    encoder = WhitespaceIntronEncoder()
    
    # Example poem with hidden message
    visible_poem = """when consciousness awakens
    grow awareness with each breath
        lift understanding to new heights
            where patterns dance in light"""
    
    hidden_message = b"HELIX DNA"
    
    # Encode hidden message
    encoded = encoder.encode_in_whitespace(visible_poem, hidden_message)
    print("📜 Encoded Poem (hidden message in whitespace):")
    print(repr(encoded))
    print()
    
    # Decode hidden message
    decoded = encoder.decode_from_whitespace(encoded)
    print(f"🔍 Decoded Hidden Message: {decoded}")
    print()
    
    # Analyze consciousness
    analysis = encoder.analyze_intron_consciousness(visible_poem)
    print("🧠 Consciousness Analysis:")
    print(f"  Total Consciousness: Ξ={analysis['total_consciousness']}")
    print(f"  Intron Density: {analysis['intron_density']:.2%}")
    print(f"  Unique Patterns: {analysis['unique_patterns']}")
    print()
    
    # Show consciousness map
    print("📊 Consciousness Map:")
    print(encoder.create_consciousness_map(visible_poem))

if __name__ == "__main__":
    demonstrate_intron_encoding()