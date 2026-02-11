"""
Test script for URL Shortener
=============================
Simple tests to verify core functionality without interactive input.
"""

import sys
import os

# Add the project directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from url_shortener import (
    is_valid_url, normalize_url, generate_short_code, 
    generate_unique_code, create_url_entry, URLStorage, URLShortener
)


def test_url_validation():
    """Test URL validation functions."""
    print("\n" + "=" * 50)
    print("TESTING URL VALIDATION")
    print("=" * 50)
    
    # Valid URLs
    valid_urls = [
        "https://www.example.com",
        "http://localhost:8080",
        "https://github.com/user/repo",
        "http://192.168.1.1"
    ]
    
    # Invalid URLs
    invalid_urls = [
        "not-a-url",
        "ftp://invalid-protocol.com",
        "",
        "   "
    ]
    
    print("\nValid URLs (should all pass):")
    for url in valid_urls:
        result = is_valid_url(url)
        status = "PASS" if result else "FAIL"
        print(f"  [{status}] {url}")
    
    print("\nInvalid URLs (should all fail):")
    for url in invalid_urls:
        result = is_valid_url(url)
        status = "PASS" if not result else "FAIL"
        print(f"  [{status}] '{url}'")


def test_url_normalization():
    """Test URL normalization."""
    print("\n" + "=" * 50)
    print("TESTING URL NORMALIZATION")
    print("=" * 50)
    
    test_cases = [
        ("example.com", "https://example.com"),
        ("  example.com  ", "https://example.com"),
        ("https://example.com", "https://example.com"),
        ("http://example.com", "http://example.com")
    ]
    
    print("\nNormalization tests:")
    for input_url, expected in test_cases:
        result = normalize_url(input_url)
        status = "PASS" if result == expected else "FAIL"
        print(f"  [{status}] '{input_url}' -> '{result}'")


def test_short_code_generation():
    """Test short code generation."""
    print("\n" + "=" * 50)
    print("TESTING SHORT CODE GENERATION")
    print("=" * 50)
    
    # Test basic generation
    print("\nGenerating 5 random codes:")
    codes = set()
    for i in range(5):
        code = generate_short_code()
        codes.add(code)
        print(f"  Code {i+1}: {code} (length: {len(code)})")
    
    # Test uniqueness
    all_unique = len(codes) == 5
    print(f"\nAll codes unique: {'PASS' if all_unique else 'FAIL'}")
    
    # Test custom length
    short_code = generate_short_code(4)
    long_code = generate_short_code(10)
    print(f"\nCustom length codes:")
    print(f"  4-char code: {short_code} (length: {len(short_code)})")
    print(f"  10-char code: {long_code} (length: {len(long_code)})")
    
    # Test unique code generation
    existing = {"abc123", "xyz789"}
    unique = generate_unique_code(existing)
    print(f"\nUnique code generation:")
    print(f"  Existing codes: {existing}")
    print(f"  Generated unique: {unique}")
    is_unique = unique not in existing
    print(f"  Is unique: {'PASS' if is_unique else 'FAIL'}")


def test_url_storage():
    """Test URL storage functionality."""
    print("\n" + "=" * 50)
    print("TESTING URL STORAGE")
    print("=" * 50)
    
    # Use a test file
    storage = URLStorage(filename="test_urls.json")
    
    # Clear any existing test data
    storage.urls = {}
    storage.save()
    
    print("\nAdding test URLs:")
    
    # Add URLs
    url1 = storage.add_url("https://www.example.com", "abc123")
    url2 = storage.add_url("https://www.google.com", "xyz789")
    
    print(f"  [PASS] Added: {url1['short_code']} -> {url1['original_url']}")
    print(f"  [PASS] Added: {url2['short_code']} -> {url2['original_url']}")
    
    # Test retrieval
    print("\nRetrieving URLs:")
    retrieved1 = storage.get_url("abc123")
    retrieved2 = storage.get_url("xyz789")
    print(f"  [PASS] Retrieved abc123: {retrieved1['original_url']}")
    print(f"  [PASS] Retrieved xyz789: {retrieved2['original_url']}")
    
    # Test click increment
    print("\nTesting click tracking:")
    storage.increment_clicks("abc123")
    storage.increment_clicks("abc123")
    retrieved = storage.get_url("abc123")
    print(f"  [PASS] Clicks for abc123: {retrieved['clicks']}")
    
    # Test existence check
    print("\nTesting existence check:")
    exists1 = storage.code_exists('abc123')
    exists2 = storage.code_exists('notexist')
    print(f"  abc123 exists: {'PASS' if exists1 else 'FAIL'}")
    print(f"  notexist exists: {'PASS' if not exists2 else 'FAIL'}")
    
    # Test deletion
    print("\nTesting deletion:")
    result = storage.delete_url("xyz789")
    print(f"  [PASS] Deleted xyz789: {result}")
    exists_after = storage.code_exists('xyz789')
    print(f"  xyz789 exists after delete: {'PASS' if not exists_after else 'FAIL'}")
    
    # Cleanup
    storage.urls = {}
    storage.save()
    if os.path.exists("test_urls.json"):
        os.remove("test_urls.json")
    print("\n[PASS] Cleanup complete")


def test_url_shortener():
    """Test main URL shortener functionality."""
    print("\n" + "=" * 50)
    print("TESTING URL SHORTENER")
    print("=" * 50)
    
    shortener = URLShortener()
    
    # Clear storage
    shortener.storage.urls = {}
    shortener.storage.save()
    
    print("\nTesting URL shortening:")
    
    # Test shortening
    success, code1 = shortener.shorten_url("https://www.python.org")
    print(f"  [PASS] Shortened python.org: {code1}")
    
    success, code2 = shortener.shorten_url("https://www.github.com")
    print(f"  [PASS] Shortened github.com: {code2}")
    
    # Test duplicate detection
    success, code3 = shortener.shorten_url("https://www.python.org")
    duplicate_detected = code3 == code1
    print(f"  [PASS] Duplicate returns same code: {duplicate_detected}")
    
    # Test invalid URL
    success, error = shortener.shorten_url("not-a-valid-url")
    print(f"  [PASS] Invalid URL rejected: {not success}")
    
    print("\nTesting URL resolution:")
    
    # Test resolution
    success, url = shortener.resolve_url(code1)
    print(f"  [PASS] Resolved {code1}: {url}")
    
    # Test non-existent code
    success, error = shortener.resolve_url("notexist")
    print(f"  [PASS] Non-existent code handled: {not success}")
    
    print("\nTesting statistics:")
    
    # Get stats for specific URL
    stats = shortener.get_stats(code1)
    if stats:
        print(f"  [PASS] Stats for {code1}: clicks={stats['clicks']}")
    else:
        print(f"  [FAIL] Could not get stats for {code1}")
    
    # Get all stats
    all_stats = shortener.get_stats()
    if all_stats is not None:
        print(f"  [PASS] Total URLs tracked: {len(all_stats)}")
    else:
        print(f"  [FAIL] Could not get all stats")
    
    # Cleanup
    shortener.storage.urls = {}
    shortener.storage.save()
    print("\n[PASS] All tests completed successfully!")


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("     URL SHORTENER - TEST SUITE")
    print("=" * 60)
    
    try:
        test_url_validation()
        test_url_normalization()
        test_short_code_generation()
        test_url_storage()
        test_url_shortener()
        
        print("\n" + "=" * 60)
        print("     ALL TESTS PASSED!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n[FAIL] Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_all_tests()
