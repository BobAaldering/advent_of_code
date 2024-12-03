#include "day_three.h"

day_three::day_three(const std::string &file_input_name) :
        advent_day(file_input_name),
        m_instructions_str {std::istreambuf_iterator<char>(m_input_file_stream), std::istreambuf_iterator<char>() },
        m_instruction_regex { R"(mul\((\d+),(\d+)\)|do(n't)?\(\))" },
        m_instructions {}
{}

auto day_three::part_one() -> long {
    auto ite = std::sregex_iterator(m_instructions_str.begin(), m_instructions_str.end(), m_instruction_regex);

    long solution = 0;

    for (; ite != std::sregex_iterator(); ++ite) {
        const std::smatch& is_match = *ite;

        if (is_match[1].matched && is_match[2].matched) {
            int op_a = std::stoi(is_match[1].str());
            int op_b = std::stoi(is_match[2].str());

            solution += op_a * op_b;

            m_instructions.emplace_back(op_a, op_b, false);
        }
        else {
            m_instructions.emplace_back(-1, -1, is_match[3].matched);
        }
    }

    return solution;
}

auto day_three::part_two() -> long {
    return std::get<0>(std::accumulate(
        m_instructions.begin(), m_instructions.end(),
        std::make_tuple(0, true),
        _fold_values
    ));
}

auto day_three::_fold_values(const std::tuple<int, bool> &state, const std::tuple<int, int, bool> &tuple) -> std::tuple<int, bool> {
    auto [s, accepting] = state;
    auto [a, b, dont] = tuple;

    if (a == -1)
        return {s, !dont};

    return accepting ? std::make_tuple(s + a * b, true) : state;
}
