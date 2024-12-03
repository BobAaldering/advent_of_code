#include <map>

#include "day_one.h"
#include "day_two.h"

int main() {
    std::map<long, std::unique_ptr<advent_day>> solutions = {};

    solutions.emplace(1, std::make_unique<day_one>("../inputs/2024/day_one.txt"));
    solutions.emplace(2, std::make_unique<day_two>("../inputs/2024/day_two.txt"));

    for (const auto& single_day : solutions) {
        std::println("--- DAY {} ---", single_day.first);

        std::println("Part one: {}", single_day.second->part_one());
        std::println("Part two: {}", single_day.second->part_two());
    }

    return EXIT_SUCCESS;
}
