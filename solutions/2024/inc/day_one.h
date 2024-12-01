#ifndef ADVENT_OF_CODE_DAY_ONE_H
#define ADVENT_OF_CODE_DAY_ONE_H

#include <ranges>
#include <algorithm>

#include "advent_day.h"

class day_one : public advent_day {
public:
    explicit day_one(const std::string& file_input_name);

    long part_one() override;
    long part_two() override;

public:
    std::vector<int> m_left;
    std::vector<int> m_right;
};

#endif
