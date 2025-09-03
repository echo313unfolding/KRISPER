#!/usr/bin/env python3
"""
KRISPER Interactive Demo - See natural language programming in action!
"""

import time
import json
from krisper import compile_text

def typewriter_print(text, delay=0.03):
    """Print text with typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def demo():
    print("\n" + "="*60)
    print(" KRISPER - Natural Language Programming Demo")
    print("="*60)
    
    typewriter_print("\nWelcome! I'll show you how to program without coding.\n")
    time.sleep(1)
    
    demos = [
        {
            "title": "1. Simple Compression",
            "input": "compress payload 'Hello World' as greeting",
            "explanation": "This tells the computer to compress the text 'Hello World' and name it 'greeting'"
        },
        {
            "title": "2. Using Parameters",
            "input": "compress payload 'secret message' using seed=42 as secret",
            "explanation": "You can add parameters like 'seed=42' to control how operations work"
        },
        {
            "title": "3. Comparing Data",
            "input": "compress payload 'apple' as a compress payload 'apple' as b compare a with b",
            "explanation": "KRISPER can compare things - here we check if two compressions are identical"
        },
        {
            "title": "4. Explaining Results",
            "input": "compress payload 'analyze this data' as result explain result",
            "explanation": "Ask KRISPER to explain what happened with any operation"
        }
    ]
    
    for demo in demos:
        print("\n" + "-"*50)
        typewriter_print(f"\n{demo['title']}")
        typewriter_print(f"\n💭 {demo['explanation']}")
        
        print(f"\n📝 You type: {demo['input']}")
        input("\nPress Enter to see the magic... ")
        
        print("\n🔮 KRISPER translates to:")
        result = json.loads(compile_text(demo['input']))
        print(json.dumps(result, indent=2))
        
        time.sleep(1)
    
    print("\n" + "="*60)
    typewriter_print("\n✨ That's KRISPER! You just programmed without writing code!")
    typewriter_print("\nNow try it yourself. Type 'python krisper.py' to start.\n")

if __name__ == "__main__":
    demo()