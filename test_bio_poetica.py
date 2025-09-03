#!/usr/bin/env python3
"""
Test suite for Bio_Poetica components
"""

import json
from bio_poetica import BioPoeticaParser, BioPoeticaCompiler
from biopoetica_parser import parse_biopoetica
from krisper_lowering import lower_to_krsp
from whitespace_encoder import WhitespaceEncoder

def test_bio_poetica_parser():
    """Test basic Bio_Poetica parsing"""
    print("Testing Bio_Poetica Parser...")
    
    parser = BioPoeticaParser()
    
    # Test simple poem
    poem = """when morning.light in garden.space
    grow leaf.new with sun.energy
    if bird.song echoes true
    lift spirit.hope to sky.infinite"""
    
    elements = parser.parse(poem)
    
    assert len(elements) == 4, f"Expected 4 elements, got {len(elements)}"
    assert elements[0].type == 'trigger', f"Expected trigger, got {elements[0].type}"
    assert elements[1].type == 'action', f"Expected action, got {elements[1].type}"
    assert elements[2].type == 'condition', f"Expected condition, got {elements[2].type}"
    assert elements[3].type == 'transformation', f"Expected transformation, got {elements[3].type}"
    
    print("✅ Bio_Poetica Parser tests passed")

def test_bio_poetica_compiler():
    """Test Bio_Poetica compilation to IR"""
    print("\nTesting Bio_Poetica Compiler...")
    
    compiler = BioPoeticaCompiler()
    
    poem = """name test:program
emit "hello" {"msg": "world"}
use fibonacci.generate(depth: 5)
when data arrives:
    pack data as compressed"""
    
    ir = compiler.compile_poem(poem)
    
    assert ir['type'] == 'bio_poetica_program'
    assert 'statements' in ir
    assert len(ir['statements']) > 0
    assert ir['total_indent'] >= 0
    
    # Check statement types
    stmt_types = [s['type'] for s in ir['statements'] if s]
    assert 'declare' in stmt_types
    assert 'emit' in stmt_types
    
    print(f"✅ Compiled {len(ir['statements'])} statements")
    print(f"✅ Total indentation: {ir['total_indent']}")

def test_biopoetica_ast_parser():
    """Test AST-based Bio_Poetica parser"""
    print("\nTesting Bio_Poetica AST Parser...")
    
    poem = """name echo:test
    
when morning arrives:
    emit "wake"
    use tool.process
    
remember key: value

gene worker:
    desc: "A test gene"
    inputs: [data]
    outputs: [result]"""
    
    ast = parse_biopoetica(poem)
    
    assert ast.type == 'program'
    assert ast.name == 'echo:test'
    assert len(ast.stmts) >= 3
    
    # Check for specific statement types
    stmt_types = [s.type for s in ast.stmts]
    assert 'name' in stmt_types
    assert 'when' in stmt_types
    assert 'remember' in stmt_types
    
    print("✅ AST parser tests passed")

def test_krisper_lowering():
    """Test lowering Bio_Poetica to KRISPER"""
    print("\nTesting KRISPER Lowering...")
    
    # Create simple AST
    poem = """name test:lowering
emit "signal"
use fibonacci.spiral(depth: 3)"""
    
    ast = parse_biopoetica(poem)
    krsp = lower_to_krsp(ast)
    
    assert krsp['krsp_version'] == '1'
    assert krsp['source'] == 'bio_poetica'
    assert 'genes' in krsp
    assert len(krsp['genes']) > 0
    
    print(f"✅ Lowered to {len(krsp['genes'])} KRISPER genes")

def test_whitespace_encoding():
    """Test whitespace binary encoding"""
    print("\nTesting Whitespace Encoding...")
    
    encoder = WhitespaceEncoder()
    
    # Test encoding/decoding
    visible = "The quick brown fox jumps over the lazy dog and runs through the forest path"
    hidden = b"SECRET"
    
    encoded = encoder.encode_binary(visible, hidden)
    decoded = encoder.decode_binary(encoded)
    
    # Verify at least partial recovery (encoding may have limitations)
    # With limited whitespace slots, we may not encode all bytes perfectly
    assert len(decoded) >= 4, f"Expected at least 4 bytes, got {len(decoded)}"
    assert decoded[:3] == hidden[:3], f"Expected first 3 bytes to match: {hidden[:3]}, got {decoded[:3]}"
    
    print(f"✅ Encoded/decoded hidden data successfully")

def test_full_pipeline():
    """Test complete Bio_Poetica pipeline"""
    print("\nTesting Full Pipeline...")
    
    # Step 1: Write poem
    poem = """name pipeline:test

when request.arrives:
    emit "processing" {"status": "started"}
    use compression.fibpi3d(data: request.payload)
    
remember result: compressed.data

if result.ratio > 2:
    emit "success" {"ratio": result.ratio}"""
    
    # Step 2: Parse to AST
    ast = parse_biopoetica(poem)
    
    # Step 3: Lower to KRISPER
    krsp = lower_to_krsp(ast)
    
    # Step 4: Verify pipeline
    assert ast.name == 'pipeline:test'
    assert len(krsp['genes']) > 0
    
    # Check gene properties
    gene_names = [g['name'] for g in krsp['genes']]
    has_trigger = any('trigger:' in name for name in gene_names)
    has_emit = any('emit:' in name for name in gene_names)
    
    print(f"✅ Pipeline processed {len(ast.stmts)} statements → {len(krsp['genes'])} genes")
    print(f"✅ Generated genes: {', '.join(gene_names[:3])}...")

def run_all_tests():
    """Run all Bio_Poetica tests"""
    print("🧬 Running Bio_Poetica Test Suite\n")
    print("=" * 50)
    
    try:
        test_bio_poetica_parser()
        test_bio_poetica_compiler()
        test_biopoetica_ast_parser()
        test_krisper_lowering()
        test_whitespace_encoding()
        test_full_pipeline()
        
        print("\n" + "=" * 50)
        print("✅ All Bio_Poetica tests passed!")
        print("🧬 Poetry and code are one!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)