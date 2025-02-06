#include <iostream>
#include <atomic>
#include <thread>
#include <vector>

// Test different C++ features based on standards
#if __cplusplus >= 202002L
    #include <concepts>
    #include <ranges>
    template<typename T>
    concept Numeric = std::integral<T> || std::floating_point<T>;
#endif

class FeatureTest {
private:
    std::atomic<int> counter{0};

public:
    void increment() {
        counter++;
    }

    void test_features() {
        std::cout << "C++ Standard: " << __cplusplus << std::endl;
        
        // Test atomic operations
        std::vector<std::thread> threads;
        for(int i = 0; i < 5; ++i) {
            threads.emplace_back([this]() {
                for(int j = 0; j < 1000; ++j) {
                    increment();
                }
            });
        }

        for(auto& thread : threads) {
            thread.join();
        }

        std::cout << "Final counter value: " << counter << std::endl;

        // Test C++20 features if available
        #if __cplusplus >= 202002L
            std::cout << "Testing C++20 features:" << std::endl;
            auto test_numeric = [](Numeric auto x) {
                return x * 2;
            };
            std::cout << "Numeric concept test: " << test_numeric(42) << std::endl;

            std::vector<int> numbers = {1, 2, 3, 4, 5};
            auto even = numbers | std::views::filter([](int n) { return n % 2 == 0; });
            std::cout << "Ranges test - Even numbers:";
            for(int n : even) {
                std::cout << " " << n;
            }
            std::cout << std::endl;
        #endif
    }
};

int main() {
    FeatureTest test;
    test.test_features();
    return 0;
}