#include "day_one.h"

day_one::day_one(const std::string &file_input_name) :
    advent_day(file_input_name),
    m_left {},
    m_right {}
{}

long day_one::part_one() {
    auto parsed_file_content = std::views::istream<int>(m_input_file_stream)
                 | std::ranges::to<std::vector>();

    m_left = std::views::iota(0U, parsed_file_content.size())
                 | std::views::filter([] (int index) { return index % 2 == 0; })
                 | std::views::transform([&parsed_file_content] (int index) { return parsed_file_content[index]; })
                 | std::ranges::to<std::vector>();

    m_right = std::views::iota(0U, parsed_file_content.size())
                 | std::views::filter([] (int index) { return index % 2 == 1; })
                 | std::views::transform([&parsed_file_content] (int index) { return parsed_file_content[index]; })
                 | std::ranges::to<std::vector>();

    std::ranges::sort(m_left);
    std::ranges::sort(m_right);

    return std::ranges::fold_left(std::views::zip(m_left, m_right), 0, [] (auto acc, auto value) {
        return acc + std::abs(value.first - value.second);
    });
}

long day_one::part_two() {
    return std::ranges::fold_left(m_left, 0, [this] (int acc, int value) {
        return acc + (value * std::ranges::count(m_right, value));
    });
}
