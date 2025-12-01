from itertools import accumulate, pairwise

def day_1(filename: str) -> tuple[int, int]:
    values = [(-1 if data[0] == "L" else 1) * int(data[1:]) for data in open(filename).read().splitlines()]
    acc_values = list(accumulate(values, initial=50))

    part_1 = sum((x % 100) == 0 for x in acc_values)
    part_2 = sum(b // 100 - a // 100 if b > a else (a - 1) // 100 - (b - 1) // 100 for a, b in pairwise(acc_values))

    return part_1, part_2
