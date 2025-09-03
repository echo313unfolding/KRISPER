#!/usr/bin/env python3
"""
KRISPER Test Suite - Verify the transpiler works correctly
"""

import json
from krisper import KrisperCompiler, ValidationError

def test_basic_compression():
    """Test basic compression operation"""
    compiler = KrisperCompiler()
    result = compiler.compile("compress payload 'hello' as r1")
    
    assert result["version"] == "0.1"
    assert len(result["plan"]) == 1
    assert result["plan"][0]["op"] == "compress"
    assert result["plan"][0]["out"] == "r1"
    print("✓ Basic compression test passed")

def test_compression_with_seed():
    """Test compression with seed parameter"""
    compiler = KrisperCompiler()
    result = compiler.compile("compress payload 'test' using seed=12345 as data")
    
    assert result["plan"][0]["params"]["seed"] == 12345
    assert result["plan"][0]["out"] == "data"
    print("✓ Compression with seed test passed")

def test_compare_operation():
    """Test compare operation"""
    compiler = KrisperCompiler()
    result = compiler.compile("compress payload 'a' as x compress payload 'b' as y compare x with y")
    
    assert len(result["plan"]) == 3
    assert result["plan"][2]["op"] == "compare"
    assert result["plan"][2]["in"]["a"] == "x"
    assert result["plan"][2]["in"]["b"] == "y"
    print("✓ Compare operation test passed")

def test_undefined_variable():
    """Test error handling for undefined variables"""
    compiler = KrisperCompiler()
    try:
        result = compiler.compile("compare x with y")
        assert False, "Should have raised ValidationError"
    except ValidationError as e:
        assert "UNDEFINED_REF" in str(e)
    print("✓ Undefined variable error test passed")

def test_empty_payload():
    """Test error handling for empty payload"""
    compiler = KrisperCompiler()
    try:
        result = compiler.compile("")
        assert False, "Should have raised ValidationError"
    except ValidationError as e:
        assert "EMPTY_PAYLOAD" in str(e)
    print("✓ Empty payload error test passed")

def test_explain_operation():
    """Test explain operation"""
    compiler = KrisperCompiler()
    result = compiler.compile("compress payload 'data' as info explain info")
    
    assert len(result["plan"]) == 2
    assert result["plan"][1]["op"] == "explain"
    assert result["plan"][1]["in"]["ref"] == "info"
    print("✓ Explain operation test passed")

def test_attest_operation():
    """Test attest operation"""
    compiler = KrisperCompiler()
    result = compiler.compile("compress payload 'document' as doc attest")
    
    assert len(result["plan"]) == 2
    assert result["plan"][1]["op"] == "attest"
    print("✓ Attest operation test passed")

def test_multiple_compressions():
    """Test multiple compression operations"""
    compiler = KrisperCompiler()
    result = compiler.compile("compress payload 'first' as a compress payload 'second' as b")
    
    assert len(result["plan"]) == 2
    assert result["plan"][0]["out"] == "a"
    assert result["plan"][1]["out"] == "b"
    print("✓ Multiple compressions test passed")

def run_all_tests():
    """Run all tests"""
    print("Running KRISPER Test Suite...")
    print("-" * 50)
    
    tests = [
        test_basic_compression,
        test_compression_with_seed,
        test_compare_operation,
        test_undefined_variable,
        test_empty_payload,
        test_explain_operation,
        test_attest_operation,
        test_multiple_compressions
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
    
    print("-" * 50)
    print(f"Tests passed: {passed}/{len(tests)}")
    
    if failed == 0:
        print("\n🎉 All tests passed! KRISPER is working correctly.")
    else:
        print(f"\n⚠️  {failed} tests failed.")

if __name__ == "__main__":
    run_all_tests()