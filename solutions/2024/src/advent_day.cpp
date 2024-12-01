#include "advent_day.h"

advent_day::advent_day(const std::string &file_input_name) :
    m_input_file_stream {file_input_name }
{
    if (!m_input_file_stream)
        throw std::runtime_error { std::format("Cannot open file '{}'!", file_input_name) };
}
