import operator
import re
import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist
from functools import reduce, cache
from itertools import accumulate, pairwise, product, groupby
from collections import Counter


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


def day_4(filename: str) -> tuple[int, int]:
    grid = open(filename).read().splitlines()
    height, width = len(grid), len(grid[0])

    neigh = [(dx, dy) for dx, dy in product((-1, 0, 1), repeat=2) if (dx, dy) != (0, 0)]
    papers = {(x, y) for y in range(height) for x in range(width) if grid[y][x] == "@"}

    def _neighbors(x, y):
        return ((x + dx, y + dy) for dx, dy in neigh if 0 <= x + dx < width and 0 <= y + dy < height)

    def _adjacent_count(position):
        return sum(nb in papers for nb in _neighbors(*position))

    def _removal_layers():
        current = accessible
        remaining = papers
        while current:
            yield current
            remaining -= current

            current = {p for p in remaining if _adjacent_count(p) < 4}

    accessible = {p for p in papers if _adjacent_count(p) < 4}

    part_1 = len(accessible)
    part_2 = sum(len(layer) for layer in _removal_layers())

    return part_1, part_2


def day_5(filename: str) -> tuple[int, int]:
    ranges_text, index_text = open(filename).read().split("\n\n")
    ranges = sorted((int(low), int(high) + 1) for low, high in re.findall(r'(\d+)-(\d+)', ranges_text))

    merged = []

    for start, end in ranges:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))

        else:
            merged.append((start, end))

    part_1 = sum(any(a <= int(i) <= b for a, b in ranges) for i in index_text.split())
    part_2 = sum(b - a + 1 for a, b in merged)

    return part_1, part_2


def day_6(filename: str) -> tuple[int, int]:
    grid = open(filename).read().splitlines()
    columns = ["".join(c) for c in zip(*[l.ljust(max(map(len, grid))) for l in grid])]
    problems = [list(g) for k, g in groupby(columns, key=lambda c: c[:-1].strip() == "") if not k]

    part_1 = 0
    part_2 = 0

    for problem in problems:
        operand = next(c[-1] for c in problem if c[-1] in "+*")

        apply_operand = sum if operand == "+" else lambda numbers: reduce(operator.mul, numbers, 1)

        part_1 += apply_operand([int(s) for r in ["".join(c[i] for c in problem) for i in range(len(grid) - 1)] if (s := r.strip())])

        part_2 += apply_operand([int(n) for c in problem[::-1] if (n := c[:-1].replace(" ", ""))])

    return part_1, part_2


def day_7(filename: str) -> tuple[int, int]:
    grid = open(filename).read().splitlines()
    height, width = len(grid), len(grid[0])
    y, x = next((y, r.find("S")) for y, r in enumerate(grid) if "S" in r)

    beams = Counter({x: 1})
    splits = set()

    for row in range(y + 1, height):
        next_beams = Counter()

        for x, count in beams.items():
            if grid[row][x] == "^":
                splits.add((row, x))
                next_beams[x - 1] += count
                next_beams[x + 1] += count

            else:
                next_beams[x] += count

        beams = Counter({x: c for x, c in next_beams.items() if 0 <= x < width})

    part_1 = len(splits)
    part_2 = sum(beams.values())

    return part_1, part_2


def day_8(filename: str) -> tuple[int, int]:
    points = np.array([list(map(int, line.split(","))) for line in open(filename) if line.strip()])
    num_points = len(points)

    i_indices, j_indices = np.triu_indices(num_points, 1)
    sorted_edge_indices = np.argsort(pdist(points))

    graph_part_1 = nx.Graph()
    graph_part_1.add_nodes_from(range(num_points))

    limit = 1000 if num_points > 20 else 10

    for idx in sorted_edge_indices[:limit]:
        graph_part_1.add_edge(i_indices[idx], j_indices[idx])

    component_sizes = sorted([len(c) for c in nx.connected_components(graph_part_1)], reverse=True)

    part_1 = int(np.prod(component_sizes[:3]))

    graph_part_2 = nx.utils.UnionFind(range(num_points))
    num_components = num_points
    last_edge = (0, 0)

    for idx in sorted_edge_indices:
        u, v = i_indices[idx], j_indices[idx]

        if graph_part_2[u] != graph_part_2[v]:
            graph_part_2.union(u, v)
            num_components -= 1

            if num_components == 1:
                last_edge = (u, v)
                break

    part_2 = int(points[last_edge[0], 0] * points[last_edge[1], 0])

    return part_1, part_2


def day_9(filename: str) -> tuple[int, int]:
    points = [tuple(map(int, line.split(","))) for line in open(filename) if line.strip()]

    part_1 = max((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1) for (x1, y1), (x2, y2) in product(points, repeat=2))

    return part_1, 0


def day_11(filename: str) -> tuple[int, int]:
    data = [re.findall(r"\w+", line) for line in open(filename) if line.strip()]
    graph = {nodes[0]: nodes[1:] for nodes in data}

    @cache
    def _count_paths(start, end):
        if start == end:
            return 1

        return sum(_count_paths(neighbor, end) for neighbor in graph.get(start, []))

    def _count_sequence(sequence):
        return reduce(operator.mul, (_count_paths(u, v) for u, v in pairwise(sequence)), 1)

    part_1 = _count_paths("you", "out")
    part_2 = _count_sequence(["svr", "fft", "dac", "out"]) + _count_sequence(["svr", "dac", "fft", "out"])

    return part_1, part_2
