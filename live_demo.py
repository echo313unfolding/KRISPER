#!/usr/bin/env python3
"""
KRISPER Live Demo - See it Actually Work!
"""

import time
import random

def execute_natural_language(command):
    """Simple executor that shows visual results"""
    
    # Simulate parsing and execution
    if "emit" in command and "sparkle" in command:
        print("   ✨✨✨ SPARKLE EFFECT ✨✨✨")
        time.sleep(0.5)
        
    elif "grow" in command:
        match = "happiness" if "happiness" in command else "something"
        print(f"   📈 Growing {match}...")
        for i in range(5):
            print(f"   {'▓' * (i+1)}")
            time.sleep(0.2)
            
    elif "celebrate" in command:
        print("   🎆 🎇 🎆 FIREWORKS! 🎆 🎇 🎆")
        time.sleep(0.5)
        
    elif "analyze" in command:
        print("   🔍 Analyzing...")
        time.sleep(0.5)
        print("   📊 Sentiment: POSITIVE")
        
    elif "respond" in command:
        print("   💬 Bot says: 'Thanks for your message!'")
        
    elif "compress" in command:
        print("   📦 Compressing data...")
        time.sleep(0.3)
        print("   ✅ Compressed: 1024 bytes → 128 bytes (87.5% saved)")

def live_demo():
    """Interactive live demonstration"""
    print("🚀 KRISPER LIVE DEMO - Natural Language in Action!")
    print("=" * 60)
    
    demos = [
        ("🎮 Game Logic Example:", [
            "when player.health < 20:",
            "    emit 'warning' {\"type\": \"low_health\"}",
            "    flash screen.border red"
        ]),
        
        ("📱 App Interaction:", [
            "when user swipes left:",
            "    animate card.sliding leftward",
            "    remove card from stack",
            "    emit 'swipe.complete'"
        ]),
        
        ("🤖 Simple AI:", [
            "analyze user.input for intent",
            "if intent is 'greeting':",
            "    respond with friendly.message",
            "remember last.interaction"
        ])
    ]
    
    for title, commands in demos:
        print(f"\n{title}")
        print("-" * 40)
        
        for cmd in commands:
            print(f"\n📝 {cmd}")
            time.sleep(0.5)
            execute_natural_language(cmd)
            
    # Interactive section
    print("\n\n🎯 TRY IT YOURSELF!")
    print("=" * 60)
    print("Type commands like:")
    print("  • emit sparkle")
    print("  • grow happiness")
    print("  • celebrate with fireworks")
    print("  • compress data")
    print("  • quit (to exit)")
    print()
    
    while True:
        try:
            command = input("krisper> ").strip().lower()
            
            if command in ['quit', 'exit']:
                print("Goodbye! 🧬")
                break
                
            if command:
                execute_natural_language(command)
                
        except KeyboardInterrupt:
            print("\nGoodbye! 🧬")
            break

if __name__ == "__main__":
    live_demo()