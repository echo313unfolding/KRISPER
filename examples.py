#!/usr/bin/env python3
"""
KRISPER Examples - Demonstrating natural language programming
"""

from krisper import KrisperCompiler, compile_text

def print_example(description, text):
    """Pretty print an example"""
    print(f"\n{'='*60}")
    print(f"Example: {description}")
    print(f"{'='*60}")
    print(f"Input:  {text}")
    print(f"Output: {compile_text(text)}")

def main():
    print("KRISPER Examples - Natural Language to Code")
    
    # Example 1: Simple compression
    print_example(
        "Simple Compression",
        "compress payload 'hello world' as greeting"
    )
    
    # Example 2: Compression with parameters
    print_example(
        "Compression with Seed",
        "compress payload 'secret data' using seed=12345 as secure"
    )
    
    # Example 3: Multiple compressions
    print_example(
        "Multiple Operations",
        "compress payload 'first file' as file1 compress payload 'second file' as file2"
    )
    
    # Example 4: Comparison
    print_example(
        "Compare Two Items",
        "compress payload 'test' as a compress payload 'test' as b compare a with b"
    )
    
    # Example 5: Chain with explain
    print_example(
        "Explain Results",
        "compress payload 'analyze this' as data explain data"
    )
    
    # Example 6: Attestation
    print_example(
        "Create Attestation",
        "compress payload 'important document' as doc attest"
    )
    
    # Example 7: Error handling
    print_example(
        "Error Example - Undefined Variable",
        "compare x with y"
    )
    
    # Example 8: Complex chain
    print_example(
        "Complex Operation Chain",
        'compress payload "user data" using seed=999 as original compress payload "user data" as duplicate compare original with duplicate as similarity explain similarity'
    )

    print("\n" + "="*60)
    print("These examples show KRISPER's ability to understand natural language")
    print("and convert it into executable operations. No coding required!")
    print("="*60)

if __name__ == "__main__":
    main()