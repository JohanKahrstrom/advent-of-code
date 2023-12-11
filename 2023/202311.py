from collections import deque

from aoc import read_lines


def print_a(lines):
    print('-' * len(lines[0]))
    for line in lines:
        print(line)
    print('-' * len(lines[0]))


def read_starfield():
    lines = read_lines('202311.txt')
    return [
        [c for c in line]
        for line in lines
    ]


def pad_starfield(stars):
    # Horizontal
    i = 0
    while i < len(stars):
        if len([c for c in stars[i] if c != '.']) == 0:
            stars = stars[:i] + [stars[i]] + stars[i:]
            i += 1
        i += 1

    # Vertical
    i = 0
    while i < len(stars[0]):
        if len([stars[n][i] for n in range(len(stars)) if stars[n][i] != '.']) == 0:
            for n in range(len(stars)):
                stars[n] = stars[n][:i] + [stars[n][i]] + stars[n][i:]
            i += 1
        i += 1

    return stars


def get_stars(starfield):
    stars = []
    for i in range(len(starfield)):
        for j in range(len(starfield[i])):
            if starfield[i][j] == '#':
                stars.append((i, j))
    return stars


def get_distance(star1, star2):
    return abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])


def get_total_distance(stars):
    distance = 0

    for i in range(len(stars)):
        for j in range(i):
            distance += get_distance(stars[i], stars[j])

    return distance


def part_one():
    starfield = pad_starfield(read_starfield())
    stars = get_stars(starfield)
    distance = get_total_distance(stars)
    print(f'Part 1: {distance}')


def expand_x_space(stars, n, padding):
    for i in range(len(stars)):
        x, y = stars[i]
        if x > n:
            stars[i] = (x + padding - 1, y)

    return stars


def expand_y_space(stars, n, padding):
    for i in range(len(stars)):
        x, y = stars[i]
        if y > n:
            stars[i] = (x, y + padding - 1)

    return stars


def pad_stars(stars, padding):
    x_counts = [0] * (max([star[0] for star in stars]) + 1)
    y_counts = [0] * (max([star[1] for star in stars]) + 1)

    for x, y in stars:
        x_counts[x] += 1
        y_counts[y] += 1

    for n in list(range(len(x_counts)))[::-1]:
        if x_counts[n] == 0:
            stars = expand_x_space(stars, n, padding)

    for n in list(range(len(y_counts)))[::-1]:
        if y_counts[n] == 0:
            stars = expand_y_space(stars, n, padding)

    return stars


def part_two():
    stars = pad_stars(get_stars(read_starfield()), 1000000)
    distance = get_total_distance(stars)

    print(f'Part 2: {distance}')


if __name__ == '__main__':
    part_two()
