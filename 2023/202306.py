import numpy as np

from utils.aoc import read_lines


def read_races():
    lines = [
        [int(n) for n in line.split(':')[1].split()]
        for line in read_lines('202306.txt')
    ]

    return [{'time': t, 'distance': d} for t, d in zip(lines[0], lines[1])]


def process_race(race):
    disc = np.sqrt(race['time'] ** 2 - 4 * race['distance']) / 2
    mid = race['time'] / 2

    min = np.ceil(mid - disc) if np.ceil(mid - disc) > (mid - disc) else mid - disc + 1
    max = np.floor(mid + disc) if np.floor(mid + disc) < (mid + disc) else mid + disc - 1

    result = max - min + 1

    return result


def part_one():
    races = read_races()

    result = np.prod([process_race(race) for race in races])

    print(f'Part 1: {result}')


def part_two():
    races = read_races()

    race = {
        'time': int(str(''.join([str(r['time']) for r in races]))),
        'distance': int(str(''.join([str(r['distance']) for r in races])))
    }

    print(f'Part 2: {process_race(race)}')


if __name__ == '__main__':
    part_two()
