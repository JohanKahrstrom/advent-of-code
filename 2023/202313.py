import numpy as np

from aoc import read_lines


pattern_map = {
    '.': 0,
    '#': 1,
}


def print_p(pattern):
    for line in pattern:
        print(''.join([str(c) for c in line]))


def flip(pattern):
    flipped = []

    for i in range(len(pattern[0])):
        acc = []
        for j in range(len(pattern)):
            acc.append(pattern[j][i])
        flipped.append(acc)

    return flipped


def read_patterns():
    lines = read_lines('202313.txt')

    patterns = []

    acc = []
    for line in lines + ['']:  # Add an empty line so the break logic is simple
        if line == '':
            flipped = flip(acc)
            patterns.append((np.array(acc), np.array(flipped)))
            acc = []
        else:
            acc.append([pattern_map.get(c) for c in line])

    return patterns


def pattern_value(pattern, test):
    left = 0
    right = len(pattern)
    for i in range(1, len(pattern)):
        width = min([abs(i - left), abs(right - i)])
        if test(pattern[i-width:i], pattern[i:i+width][::-1]):
            return i
    return -1


def mirror_value(left, right, test):
    left_value = pattern_value(left, test)
    if left_value > 0:
        return left_value * 100
    else:
        return pattern_value(right, test)


def mirror_test(left, right):
    return np.array_equal(left, right)


def part_one():
    patterns = read_patterns()

    result = 0
    for left, right in patterns:
        result += mirror_value(left, right, mirror_test)

    print(f'Part one: {result}')


def smudge_test(left, right):
    return np.abs(left - right).sum() == 1


def part_two():
    patterns = read_patterns()

    result = 0
    for left, right in patterns:
        result += mirror_value(left, right, smudge_test)

    print(f'Part two: {result}')


if __name__ == '__main__':
    part_one()
    part_two()
