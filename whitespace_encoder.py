#!/usr/bin/env python3
"""
Whitespace Encoder
Simple binary encoding in whitespace for metadata
"""

import re
from typing import List, Tuple, Dict, Any

class WhitespaceEncoder:
    """Encode and decode binary data in whitespace"""
    
    def __init__(self):
        # Binary encoding map
        self.encoding_map = {
            '00': ' ',      # Single space
            '01': '  ',     # Double space
            '10': '\t',     # Tab
            '11': '\t ',    # Tab + space
        }
        
    def encode_binary(self, visible_text: str, binary_data: bytes) -> str:
        """Encode binary data in the whitespace of visible text"""
        # Convert to binary string
        binary = ''.join(format(byte, '08b') for byte in binary_data)
        
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
    
    def decode_binary(self, text: str) -> bytes:
        """Decode binary data from whitespace patterns"""
        # Find all whitespace sequences
        patterns = []
        for match in re.finditer(r'(\s+)', text):
            patterns.append(match.group(1))
        
        # Reverse mapping
        decoding_map = {v: k for k, v in self.encoding_map.items()}
        
        # Extract binary data
        binary = ''
        for ws in patterns:
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

def demonstrate_encoding():
    """Show whitespace binary encoding"""
    print("🔲 WHITESPACE BINARY ENCODING")
    print("=" * 50)
    
    encoder = WhitespaceEncoder()
    
    # Example text with hidden binary
    visible_text = "when code flows through natural language"
    hidden_data = b"META"
    
    # Encode
    encoded = encoder.encode_binary(visible_text, hidden_data)
    print("📝 Visible Text:")
    print(repr(visible_text))
    print("\n🔢 Hidden Binary:", hidden_data)
    print("\n📦 Encoded (binary in whitespace):")
    print(repr(encoded))
    
    # Decode
    decoded = encoder.decode_binary(encoded)
    print(f"\n🔍 Decoded: {decoded}")

if __name__ == "__main__":
    demonstrate_encoding()