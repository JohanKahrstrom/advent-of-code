from itertools import chain, combinations

import networkx as nx

from aoc import read_lines


def read_fuel_requirements():
    lines = read_lines('20221225.txt')

    return lines


snafu_map = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2
}


def from_snafu(snafu):
    total = 0
    for i, c in enumerate(snafu[::-1]):
        total += (5 ** i) * snafu_map[c]
    return total


number_map = {
    -2: '=',
    -1: '-',
    0: '0',
    1: '1',
    2: '2'
}


def to_snafu(number):
    chars = []
    while number > 0:
        rest = (number + 2) % 5 - 2
        number = (number - rest) // 5
        chars.append(number_map[rest])
    return ''.join(chars[::-1])


def part_one():
    requrements = read_fuel_requirements()

    total = sum([from_snafu(snafu) for snafu in requrements])
    print(f'Part 1: {to_snafu(total)}')



def part_two():
    pass


if __name__ == '__main__':
    part_one()