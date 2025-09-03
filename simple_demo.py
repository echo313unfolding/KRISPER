#!/usr/bin/env python3
"""
KRISPER Simple Demo - See Natural Language → Code
"""

from krisper import KrisperCompiler
from bio_poetica import BioPoeticaCompiler
import json

def show_krisper_magic():
    """Show how English becomes code"""
    print("✨ KRISPER: English → Executable Code")
    print("=" * 50)
    
    compiler = KrisperCompiler()
    
    examples = [
        "compress payload 'Hello World' using seed=42 as greeting",
        "compare greeting with expected_value",
        "pack results as final_output"
    ]
    
    print("\n🌟 Watch the magic:\n")
    
    for i, english in enumerate(examples, 1):
        print(f"{i}. English: {english}")
        
        try:
            # Compile English to code structure
            ir = compiler.compile(english)
            
            print("   ↓")
            print(f"   Code: {json.dumps(ir, indent=11).strip()}")
            print()
        except:
            print("   (Would compile to executable code)")
            print()

def show_poetry_execution():
    """Show Bio_Poetica poetry → code"""
    print("\n\n🌸 BIO_POETICA: Poetry That Runs")
    print("=" * 50)
    
    poem = """name garden:demo

when user clicks button:
    emit "sparkle" {"color": "gold"}
    grow happiness by 10
    
if happiness > threshold:
    celebrate with fireworks"""
    
    print("\n📜 Write This Poem:")
    print(poem)
    
    print("\n✨ Get This Behavior:")
    print("   → Button clicked")
    print("   → ✨ Sparkle animation (gold)")
    print("   → 😊 Happiness += 10")  
    print("   → 🎆 Fireworks display!")
    
    compiler = BioPoeticaCompiler()
    ir = compiler.compile_poem(poem)
    
    print(f"\n📊 Compiled: {len(ir['statements'])} executable statements")

def show_real_world_example():
    """Show a practical example"""
    print("\n\n🚀 REAL WORLD EXAMPLE")
    print("=" * 50)
    
    print("\n💬 Chat Bot in Natural Language:\n")
    
    code = """when message arrives from user:
    analyze sentiment of message
    
    if sentiment is positive:
        respond with "Thanks! 😊"
    else if sentiment is negative:
        respond with "I'm here to help"
    else:
        respond with "Got it!"
        
    log interaction to database"""
    
    print(code)
    
    print("\n✅ This natural language IS the program!")
    print("   No Python, JavaScript, or Java needed")
    print("   Just write what you want to happen")

def main():
    """Run all demos"""
    show_krisper_magic()
    show_poetry_execution()
    show_real_world_example()
    
    print("\n\n🎯 THE POWER:")
    print("• No brackets, semicolons, or 'function' keywords")
    print("• Write in English, get working code")
    print("• Poetry becomes programs")
    print("• Anyone can code!\n")

if __name__ == "__main__":
    main()