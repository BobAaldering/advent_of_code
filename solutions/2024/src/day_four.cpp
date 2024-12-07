#include "day_four.h"

#include <iostream>

day_four::day_four(const std::string &file_input_name) :
    advent_day(file_input_name),
    m_field {},
    m_word { "XMAS" }
{}

auto day_four::part_one() -> long {
    std::string line {};

    while (std::getline(m_input_file_stream, line)) {
        if (!line.empty()) {
            std::stringstream sstream { line };
            m_field.m_grid.emplace_back(std::views::istream<char>(sstream) | std::ranges::to<std::vector>());
        }
    }

    std::vector<std::pair<int, int>> directions = {
        { 1, 0 },   // Right.
        { 0, 1 },   // Down.
        { 1, 1 },   // Diagonal bottom right.
        { -1, 1 },  // Diagonal bottom left.
        { 1, -1 },  // Diagonal upper right.
        { -1, -1 }, // Diagonal upper left.
        { -1, 0 },  // Left.
        { 0, -1 },  // Up.
    };

    auto is_valid_word = [&] (std::size_t x, std::size_t y, const std::pair<int, int>& dir) {
        return std::ranges::all_of(
            std::views::iota(0U, m_word.size()), [&] (int i) {
                std::size_t nx = x + i * dir.second;
                std::size_t ny = y + i * dir.first;

                return m_field.is_inside(nx, ny) && m_field(nx, ny) == m_word[i];
            });
    };

    return std::accumulate(
        std::views::iota(0UL, m_field.height()).begin(),
        std::views::iota(0UL, m_field.height()).end(),
        0U,
        [&] (std::size_t sum, std::size_t y) {
            return sum + std::accumulate(
                std::views::iota(0UL, m_field.width()).begin(),
                std::views::iota(0UL, m_field.width()).end(),
                0U,
                [&] (std::size_t inner_sum, std::size_t x) {
                    return inner_sum + std::ranges::count_if(directions, [&] (const auto& dir) {
                        return is_valid_word(x, y, dir);
                    });
                });
        });
}

auto day_four::part_two() -> long {
    auto is_valid_xmas = [&] (std::size_t x, std::size_t y) {
        if (!m_field.is_inside(x - 1, y - 1) || !m_field.is_inside(x + 1, y + 1))
            return false;

        std::string first_diagram {
            m_field(x - 1, y + 1),
            m_field(x, y),
            m_field(x + 1, y - 1)
        };

        std::string second_diagram {
            m_field(x - 1, y - 1),
            m_field(x, y),
            m_field(x + 1, y + 1)
        };

        return (first_diagram == "MAS" || first_diagram == "SAM") &&
               (second_diagram == "MAS" || second_diagram == "SAM");
    };

    return std::accumulate(
        std::views::iota(1UL, m_field.height() - 1).begin(),
        std::views::iota(1UL, m_field.height() - 1).end(),
        0L,
        [&] (int sum, int y) {
            return sum + std::accumulate(
                std::views::iota(1UL, m_field.width() - 1).begin(),
                std::views::iota(1UL, m_field.width() - 1).end(),
                0,
                [&](int inner_sum, int x) {
                    return inner_sum + (is_valid_xmas(x, y) ? 1 : 0);
                });
        });
}

