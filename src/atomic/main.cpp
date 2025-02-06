#include <iostream>
#include <vector>
#include <string>
#include <thread>
#include <atomic>

int threadCount = 100;
int iterations = 1000000;

std::atomic<int> counter = 0;

int main() {
    auto increment = []() {

        for (int i = 0; i < iterations; ++i) {
            counter++;
            auto memeSmth = std::to_string(counter);
            // TODO: Add string manipulation here for server load
        }
    };

    std::vector<std::thread> threads;
    for (int i = 0; i < threadCount; ++i) {
        threads.emplace_back(increment);
    }

    for (auto& thread : threads) {
        thread.join();
    }

    std::cout << "Counter: " << counter << std::endl;

    return 0;
}
