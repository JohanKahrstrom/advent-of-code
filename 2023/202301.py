import re

from aoc import read_lines


def part_one():
    numbers = ([
        [c for c in line if c.isnumeric()]
        for line in read_lines('202301.txt')
    ])

    to_sum = ([
        int(''.join([n[0], n[-1]])) for n in numbers
    ])

    out = sum(to_sum)

    print(f'Part 1: {out}')


def find_numbers(string):
    mapping = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    i = re.finditer(r'(?=([0-9]|zero|one|two|three|four|five|six|seven|eight|nine|ten))', string)

    return [mapping.get(match.group(1)) for match in i]


def part_two():
    numbers = [
        find_numbers(line)
        for line in read_lines('202301.txt')
    ]

    to_sum = ([
        int(''.join([n[0], n[-1]])) for n in numbers
    ])

    out = sum(to_sum)

    print(f'Part 2: {out}')


if __name__ == '__main__':
    part_two()
