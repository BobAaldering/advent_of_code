#ifndef ADVENT_OF_CODE_DAY_THREE_H
#define ADVENT_OF_CODE_DAY_THREE_H

#include <regex>
#include <numeric>

#include "advent_day.h"

class day_three : public advent_day {
public:
    explicit day_three(const std::string& file_input_name);

    auto part_one() -> long override;
    auto part_two() -> long override;

private:
    static auto _fold_values(const std::tuple<int, bool>& state, const std::tuple<int, int, bool>& tuple) -> std::tuple<int, bool>;

    std::string m_instructions_str;
    std::regex m_instruction_regex;
    std::vector<std::tuple<int, int, bool>> m_instructions;
};

#endif
