#!/usr/bin/env python3
"""
KRISPER Quick Start - Your first natural language program!
"""

from krisper import compile_text

print("""
╔═══════════════════════════════════════════════════════╗
║               KRISPER - Quick Start Guide             ║
╚═══════════════════════════════════════════════════════╝

Welcome! Let's write your first program in plain English.

Try typing one of these commands:

1. compress payload 'my first program' as hello
2. compress payload 'test data' using seed=999 as test
3. compare hello with test

""")

while True:
    try:
        command = input("krisper> ")
        if command.lower() in ['quit', 'exit']:
            print("\nGoodbye! 👋")
            break
            
        if not command.strip():
            continue
            
        result = compile_text(command)
        print("\n✨ Output:")
        print(result)
        print()
        
    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")
        break
    except Exception as e:
        print(f"\n❌ Error: {e}\n")