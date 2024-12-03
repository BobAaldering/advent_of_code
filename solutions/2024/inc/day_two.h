#ifndef ADVENT_OF_CODE_DAY_TWO_H
#define ADVENT_OF_CODE_DAY_TWO_H

#include <ranges>
#include <sstream>
#include <algorithm>

#include "advent_day.h"

class day_two : public advent_day {
public:
    explicit day_two(const std::string& file_input_name);

    auto part_one() -> long override;
    auto part_two() -> long override;

private:
    static auto _is_safe(const std::vector<int>& lines) -> bool;

    std::vector<std::vector<int>> m_reports;
};

#endif
