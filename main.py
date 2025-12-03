import importlib
import time

def get_configuration(*years: str) -> dict:
    def _discover(year):
        module = importlib.import_module(f"{year}.solutions")
        return sorted([getattr(module, n) for n in dir(module) if n.startswith("day_")], key=lambda f: int(f.__name__.split("_")[1]))
    
    return {year: _discover(year) for year in years}


def run_configuration(configuration: dict) -> None:
    for year, day_solvers in configuration.items():
        print(f"\n{'═' * 30}")
        print(f" 🎄 Advent of Code {year}")
        print(f"{'═' * 30}")

        for day in day_solvers:
            day_number = day.__name__.split("_")[1]

            # try:
            init_time = time.process_time_ns()
            part_1, part_2 = day(f"{year}/input/day_{day_number}.txt")
            elapsed_ms = (time.process_time_ns() - init_time) / 1e6

            print(f"\n  📅 Day {day_number}")
            print(f"  ├── Part 1: {part_1}")
            print(f"  ├── Part 2: {part_2}")
            print(f"  └── Time:   {elapsed_ms:.3f} ms")

            # except Exception as error:
            #     print(f"  An error occurred when running day {day_number}: {error}")


if __name__ == '__main__':
    advent_of_code_config = get_configuration("2025")

    run_configuration(advent_of_code_config)
