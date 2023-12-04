import re

from aoc import read_lines


def get_engine():
    return read_lines('202303.txt')


def get_numbers_map(engine):
    numbers_map = {}

    for x, line in enumerate(engine):
        i = re.finditer(r'([0-9]+)', line)

        for match in i:
            number = int(match.group(0))
            y_start = match.span()[0]
            for y in range(match.span()[0], match.span()[1]):
                # We save the coordinate along with the number, to be able to differentiate later
                numbers_map[(x, y)] = (x, y_start, number)

    return numbers_map


def get_numbers(x, numbers_map, match):
    numbers = set()

    y = match.span()[0]
    for tx in range(x - 1, x + 2):
        for ty in range(y - 1, y + 2):
            if (tx, ty) in numbers_map:
                numbers.add(numbers_map.get((tx, ty)))

    return numbers


def part_one():
    engine = get_engine()
    numbers_map = get_numbers_map(engine)
    # Dictionary from coordinates to numbers they contain

    numbers = set()

    for x, line in enumerate(engine):
        i = re.finditer(r'([^0-9.])', line)

        for match in i:
            numbers.update(get_numbers(x, numbers_map, match))

    print(f'Part 1: {sum([n for _, _, n in numbers])}')


def part_two():
    engine = get_engine()
    numbers_map = get_numbers_map(engine)
    # Dictionary from coordinates to numbers they contain

    gear_ratios = 0

    for x, line in enumerate(engine):
        i = re.finditer(r'\*', line)

        for match in i:
            numbers = [n for _, _, n in get_numbers(x, numbers_map, match)]
            if len(numbers) == 2:
                gear_ratios += numbers[0] * numbers[1]

    print(f'Part 2: {gear_ratios}')


if __name__ == '__main__':
    part_two()
