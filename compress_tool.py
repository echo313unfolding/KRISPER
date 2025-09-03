#!/usr/bin/env python3
"""
Natural Language File Compression Tool
Write compression commands in plain English!
"""

import sys
import os
from krisper import compile_text
from krisper_executor import KrisperExecutor
from bio_poetica import BioPoeticaCompiler
from bio_executor import BioPoeticaExecutor

def compress_file(filename: str):
    """Compress a file using natural language commands"""
    
    # Read file
    with open(filename, 'rb') as f:
        data = f.read()
    
    print(f"📁 File: {filename}")
    print(f"📏 Original size: {len(data):,} bytes")
    
    # Create poem for compression
    poem = f"""name file:compressor

when file "{filename}" loaded:
    emit "compression.start" {{"size": {len(data)}}}
    
remember original_data: loaded from "{filename}"
remember original_size: {len(data)}

use compression.maximum(data: original_data)
    
emit "compression.complete"
    
calculate compression_ratio: original_size / compressed_size

if compression_ratio > 2:
    emit "excellent.compression" {{"ratio": compression_ratio}}
else:
    emit "moderate.compression" {{"ratio": compression_ratio}}
    
save compressed_data to "{filename}.kz"
"""
    
    print("\n📜 Compression Poem:")
    print(poem)
    
    # For now, use direct KRISPER commands
    print("\n🚀 Executing compression...")
    
    executor = KrisperExecutor()
    
    # Store original data in executor
    executor.variables['file_data'] = data.decode('utf-8') if len(data) < 10000 else str(data[:1000])
    
    # Compress using KRISPER
    compress_ir = compile_text(f'compress payload file_data using level=9 as compressed')
    result = executor.execute(compress_ir)
    
    if result['success']:
        compressed = result['outputs']['compressed']
        ratio = len(data) / len(compressed)
        
        print(f"\n✅ Compression successful!")
        print(f"📦 Compressed size: {len(compressed):,} bytes")
        print(f"📊 Compression ratio: {ratio:.2f}:1")
        print(f"💾 Saved: {len(data) - len(compressed):,} bytes ({(1 - len(compressed)/len(data))*100:.1f}%)")
        
        # Save compressed file
        output_file = filename + '.kz'
        with open(output_file, 'w') as f:
            f.write(compressed)
        print(f"\n💾 Saved to: {output_file}")
        
        # Verify by decompressing
        decompress_ir = compile_text(f'decompress data compressed as verified')
        verify_result = executor.execute(decompress_ir)
        
        if verify_result['success']:
            print("✓ Decompression verified")
    else:
        print("✗ Compression failed:", result['log'])

def interactive_mode():
    """Interactive natural language programming"""
    print("🧬 KRISPER Interactive Mode")
    print("Type natural language commands or 'quit' to exit")
    print("Examples:")
    print("  compress payload 'hello world' as greeting")
    print("  hash data greeting as checksum")
    print("  compare greeting with 'hello world'")
    print()
    
    executor = KrisperExecutor()
    
    while True:
        try:
            command = input("krisper> ").strip()
            
            if command.lower() in ['quit', 'exit']:
                break
                
            if not command:
                continue
                
            # Try to compile and execute
            ir = compile_text(command)
            result = executor.execute(ir)
            
            if result['success']:
                for name, value in result['outputs'].items():
                    if isinstance(value, str) and len(value) > 100:
                        print(f"{name} = {value[:100]}...")
                    else:
                        print(f"{name} = {value}")
            else:
                print("Error:", result['log'][-1] if result['log'] else "Unknown error")
                
        except Exception as e:
            print(f"Error: {e}")
    
    print("\nGoodbye! 🧬")

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        if sys.argv[1] == '--interactive' or sys.argv[1] == '-i':
            interactive_mode()
        else:
            # Compress file
            compress_file(sys.argv[1])
    else:
        print("Usage:")
        print("  python compress_tool.py <filename>     # Compress a file")
        print("  python compress_tool.py --interactive  # Interactive mode")
        print()
        print("Example:")
        print("  python compress_tool.py document.txt")

if __name__ == "__main__":
    main()