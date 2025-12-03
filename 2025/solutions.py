from itertools import accumulate, pairwise


def day_1(filename: str) -> tuple[int, int]:
    values = [(-1 if data[0] == "L" else 1) * int(data[1:]) for data in open(filename).read().splitlines()]
    acc_values = list(accumulate(values, initial=50))

    part_1 = sum((x % 100) == 0 for x in acc_values)
    part_2 = sum(b // 100 - a // 100 if b > a else (a - 1) // 100 - (b - 1) // 100 for a, b in pairwise(acc_values))

    return part_1, part_2


def day_2(filename: str) -> tuple[int, int]:
    ranges = [tuple(map(int, line.strip().split('-'))) for line in open(filename).read().split(',')]

    def _repeated_numbers_in_range(a: int, b: int, max_repetition: int):
        results = []
        a_str, b_str = str(a), str(b)
        max_len = len(b_str)

        for length in range(len(a_str), max_len + 1):
            for repeat_count in range(2, max_repetition + 1):
                if length % repeat_count != 0:
                    continue

                prefix_len = length // repeat_count
                start = int(a_str[:prefix_len]) if length == len(a_str) else 10 ** (prefix_len - 1)
                end = int(b_str[:prefix_len]) if length == len(b_str) else 10 ** prefix_len - 1

                for p in range(start, end + 1):
                    n = int(str(p) * repeat_count)

                    if a <= n <= b:
                        results.append(n)
        return results

    part_1 = sum(set(n for a, b in ranges for n in _repeated_numbers_in_range(a, b, 2)))
    part_2 = sum(set(n for a, b in ranges for n in _repeated_numbers_in_range(a, b, max(len(str(b)), 2))))

    return part_1, part_2



def day_3(filename: str) -> tuple[int, int]:
    joltage_banks = [[int(c) for c in line.strip()] for line in open(filename).read().splitlines()]

    def _max_joltage(bank: list[int], n: int):
        if n == 1:
            return max(bank)

        max_digit, idx = max((bank[i], -i) for i in range(len(bank) - n + 1))
        rest = _max_joltage(bank[1 - idx:], n - 1)

        return max_digit * 10**(n - 1) + rest

    part_1 = sum(_max_joltage(bank, 2) for bank in joltage_banks)
    part_2 = sum(_max_joltage(bank, 12) for bank in joltage_banks)

    return part_1, part_2
