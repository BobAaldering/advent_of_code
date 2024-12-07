cmake_minimum_required(VERSION 3.30)
project(advent_of_code)

add_executable(advent_of_code)

set(target advent_of_code)

target_sources(
        ${target}
        PRIVATE
                main.cpp

                solutions/2024/src/day_one.cpp
                solutions/2024/src/day_two.cpp
                solutions/2024/src/day_three.cpp
                solutions/2024/src/day_four.cpp
                solutions/2024/src/advent_day.cpp
)

target_compile_features(${target} PRIVATE cxx_std_23)
set_target_properties(${target} PROPERTIES CXX_EXTENSIONS OFF)

include_directories(
        solutions/2024/inc
)

target_compile_options(
        ${target}
        PRIVATE
                $<$<CXX_COMPILER_ID:GNU,Clang,AppleClang>:-Wall -Wextra -Wpedantic -Werror -fno-omit-frame-pointer>
                $<$<AND:$<CXX_COMPILER_ID:GNU,Clang,AppleClang>,$<CONFIG:Release>>:-O3>
                $<$<AND:$<CXX_COMPILER_ID:GNU,Clang,AppleClang>,$<CONFIG:Debug>>:>
)

target_compile_options(
        ${target}
        PRIVATE
                $<$<CXX_COMPILER_ID:MSVC>:/Wall>
                $<$<AND:$<CXX_COMPILER_ID:MSVC>,$<CONFIG:Release>>:/O2>
                $<$<AND:$<CXX_COMPILER_ID:MSVC>,$<CONFIG:Debug>>:/RTC1 /Od /Zi>
)

option(USE_ASAN "Use the address sanitizer, if available" ON)

execute_process(
        COMMAND "${CMAKE_CXX_COMPILER}" -print-file-name=libasan.so
        OUTPUT_VARIABLE LIBASAN_PATH
        RESULT_VARIABLE LIBASAN_RESULT
        OUTPUT_STRIP_TRAILING_WHITESPACE
)

set(HAS_ASAN FALSE)

if (USE_ASAN AND (${LIBASAN_RESULT} EQUAL 0) AND (NOT ${LIBASAN_PATH} STREQUAL ""))
        message(NOTICE "Address sanitizer ('libasan.so') found at '${LIBASAN_PATH}'")
        set(HAS_ASAN TRUE)
endif ()

if (HAS_ASAN AND USE_ASAN)
        target_compile_options(${target} PRIVATE -fsanitize=address)
        target_link_options(${target} PRIVATE -fsanitize=address)
endif ()
