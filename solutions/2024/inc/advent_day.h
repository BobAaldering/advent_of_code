#ifndef ADVENT_OF_CODE_ADVENT_DAY_H
#define ADVENT_OF_CODE_ADVENT_DAY_H

#include <fstream>

class advent_day {
public:
    explicit advent_day(const std::string& file_input_name);

    virtual long part_one() = 0;
    virtual long part_two() = 0;

    virtual ~advent_day() = default;

protected:
    std::ifstream m_input_file_stream;
};

#endif
