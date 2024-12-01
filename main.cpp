#include "day_one.h"

int main() {
    std::vector<std::unique_ptr<advent_day>> solutions = {};

    solutions.emplace_back(std::make_unique<day_one>("../inputs/2024/day_one.txt"));

    for (const auto& single_day : solutions) {
        std::println("Part one: {}", single_day->part_one());
        std::println("Part two: {}", single_day->part_two());
    }

    return EXIT_SUCCESS;
}
