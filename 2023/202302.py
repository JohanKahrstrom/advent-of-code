import numpy as np

from aoc import read_lines


color_dim_map = {
    'red': 0,
    'green': 1,
    'blue': 2
}


def parse_games():
    lines = read_lines('202302.txt')

    games = []
    for game in lines:
        cube_sets = []
        for cube_set in game.split(':')[1].split(';'):
            a = np.zeros(3, dtype=int)
            for color_count in cube_set.split(','):
                _, count, color = color_count.split(' ')
                a[color_dim_map.get(color)] = int(count)
            cube_sets.append(a)
        games.append(cube_sets)

    return games


def is_possible(game):
    limit = np.array([12, 13, 14])
    for cube_set in game:
        if (cube_set > limit).sum() > 0:
            return False
    return True


def part_one():
    games = parse_games()

    sum = 0
    for i, game in enumerate(games):
        if is_possible(game):
            sum += i + 1

    print(f'Part 1: {sum}')


def get_game_power(game):
    current_min = np.array([0, 0, 0])

    for cube_set in game:
        current_min = np.max(np.stack([cube_set, current_min]), axis=0)

    return current_min.prod()


def part_two():
    games = parse_games()

    result = sum([get_game_power(game) for game in games])

    print(f'Part 2: {result}')


if __name__ == '__main__':
    part_two()
