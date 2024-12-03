#include "day_two.h"

day_two::day_two(const std::string &file_input_name) :
        advent_day(file_input_name),
        m_reports {}
{}

auto day_two::part_one() -> long {
    std::string line {};

    while (std::getline(m_input_file_stream, line)) {
        if (!line.empty()) {
            std::stringstream sstream { line };
            m_reports.emplace_back(std::views::istream<int>(sstream) | std::ranges::to<std::vector>());
        }
    }

    return std::ranges::count_if(m_reports, [] (const std::vector<int>& lines) { return _is_safe(lines); });
}

auto day_two::part_two() -> long {
    return std::ranges::count_if(m_reports, [] (const std::vector<int>& lines) {
        return std::ranges::any_of(std::views::iota(0U, lines.size()), [&lines] (int i) {
            std::vector<int> temp = lines;
            temp.erase(temp.begin() + i);
            return _is_safe(temp);
        });
    });
}


auto day_two::_is_safe(const std::vector<int> &lines) -> bool {
    auto increasing = std::ranges::adjacent_find(lines, [](int a, int b) { return b - a <= 0 || b - a > 3; }) == lines.end();
    auto decreasing = std::ranges::adjacent_find(lines, [](int a, int b) { return a - b <= 0 || a - b > 3; }) == lines.end();

    return increasing || decreasing;
}
