#!/usr/bin/env python3

import os
import sys
from pathlib import Path
from typing import List, Dict, Optional

class TestGenerator:
    def __init__(self, cpp_standard: str = "20"):
        self.cpp_standard = cpp_standard
        self.test_template = '''
#include <cassert>
#include <iostream>
#include <chrono>
#include <thread>
#include <atomic>
#include <memory>

// Test case template for {feature_name}
void test_{feature_name}() {{
    // Setup
    std::cout << "Running test for {feature_name}...\n";
    
    // Test implementation
    {test_implementation}
    
    std::cout << "Test {feature_name} passed!\n";
}}

// Performance benchmark
void benchmark_{feature_name}() {{
    auto start = std::chrono::high_resolution_clock::now();
    
    // Benchmark implementation
    {benchmark_implementation}
    
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "Benchmark {feature_name} completed in " << duration.count() << " microseconds\n";
}}

int main() {{
    try {{
        test_{feature_name}();
        benchmark_{feature_name}();
        std::cout << "All tests passed!\n";
        return 0;
    }} catch (const std::exception& e) {{
        std::cerr << "Test failed: " << e.what() << std::endl;
        return 1;
    }}
}}
'''

    def generate_atomic_test(self, feature_name: str, test_impl: str, bench_impl: str) -> str:
        """Generate a test file for atomic operations."""
        return self.test_template.format(
            feature_name=feature_name,
            test_implementation=test_impl,
            benchmark_implementation=bench_impl
        )

    def generate_memory_test(self) -> str:
        """Generate memory safety test."""
        test_impl = '''
        std::shared_ptr<int> ptr = std::make_shared<int>(42);
        assert(ptr.use_count() == 1);
        {
            auto ptr2 = ptr;
            assert(ptr.use_count() == 2);
        }
        assert(ptr.use_count() == 1);
        '''
        
        bench_impl = '''
        for(int i = 0; i < 10000; ++i) {
            std::shared_ptr<int> p = std::make_shared<int>(i);
        }
        '''
        
        return self.generate_atomic_test("memory_safety", test_impl, bench_impl)

    def generate_atomic_operations_test(self) -> str:
        """Generate atomic operations test."""
        test_impl = '''
        std::atomic<int> counter(0);
        std::thread t1([&counter]() {
            for(int i = 0; i < 1000; ++i) {
                counter++;
            }
        });
        std::thread t2([&counter]() {
            for(int i = 0; i < 1000; ++i) {
                counter++;
            }
        });
        t1.join();
        t2.join();
        assert(counter == 2000);
        '''
        
        bench_impl = '''
        std::atomic<int> counter(0);
        for(int i = 0; i < 100000; ++i) {
            counter.fetch_add(1, std::memory_order_relaxed);
        }
        '''
        
        return self.generate_atomic_test("atomic_operations", test_impl, bench_impl)

def create_test_file(output_dir: str, filename: str, content: str) -> None:
    """Create a test file in the specified directory."""
    test_path = Path(output_dir) / filename
    test_path.parent.mkdir(parents=True, exist_ok=True)
    test_path.write_text(content)
    print(f"Created test file: {test_path}")

def main():
    generator = TestGenerator()
    
    # Generate test files
    tests = [
        ("memory_test.cpp", generator.generate_memory_test()),
        ("atomic_test.cpp", generator.generate_atomic_operations_test())
    ]
    
    # Create test files in the src/atomic directory
    for filename, content in tests:
        create_test_file("src/atomic", filename, content)

if __name__ == "__main__":
    main()