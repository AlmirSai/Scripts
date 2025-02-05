#include <iostream>
#include <vector>
#include <string>
#include <thread>
#include <mutex>

int threadCount = 100;
int iterations = 1000000;

int counter = 0;

std::mutex m;

int main() {
    auto increment = []() {
        std::lock_guard<std::mutex> g(m);
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
