#ifndef ADVENT_OF_CODE_DAY_FOUR_H
#define ADVENT_OF_CODE_DAY_FOUR_H

#include <ranges>
#include <sstream>
#include <algorithm>
#include <numeric>

#include "advent_day.h"

class day_four : public advent_day {
public:
    explicit day_four(const std::string& file_input_name);

    auto part_one() -> long override;
    auto part_two() -> long override;

private:
    struct char_field {
        [[nodiscard]] bool is_inside(std::size_t x, std::size_t y) const {
            return x < m_grid[0].size() && y < m_grid.size();
        }

        [[nodiscard]] char operator() (std::size_t x, std::size_t y) const {
            return m_grid[x][y];
        }

        [[nodiscard]] std::size_t height() const {
            return m_grid.size();
        }

        [[nodiscard]] std::size_t width() const {
            return m_grid[0].size();
        }

        std::vector<std::vector<char>> m_grid;
    };

    char_field m_field;
    std::string m_word;
};

#endif
