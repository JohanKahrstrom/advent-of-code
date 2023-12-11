from collections import deque

from aoc import read_lines


def read_oasis():
    lines = read_lines('202309_test.txt')

    oases = []

    for line in lines:
        oases.append([int(i) for i in line.split()])

    return oases


def get_full_oases(oases):
    agg = [oases]
    while sum([abs(i) for i in agg[-1]]) > 0:
        next = [b - a for a, b in zip(agg[-1][:-1], agg[-1][1:])]
        agg.append(next)
    return agg


def calculate_ex(oasis):
    agg = get_full_oases(oasis)

    return sum(a[-1] for a in agg)


def calculate_ox(oasis):
    agg = get_full_oases(oasis)

    return sum([(-1) ** i * a[0] for i, a in enumerate(agg)])


def part_one():
    oases = read_oasis()

    result = sum([calculate_ex(oasis) for oasis in oases])

    print(f'Part one: {result}')


def part_two():
    oases = read_oasis()

    result = sum([calculate_ox(oasis) for oasis in oases])

    print(f'Part two: {result}')


if __name__ == '__main__':
    part_two()
