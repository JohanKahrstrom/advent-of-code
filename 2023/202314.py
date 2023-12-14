from utils.aoc import read_lines


def read_rocks():
    lines = read_lines('202314.txt')

    return [
        [c for c in line]
        for line in lines
    ]


def calculate_weight_north(rocks):
    max_w = len(rocks)
    total_weight = 0
    for i in range(len(rocks)):
        for j in range(len(rocks[i])):
            if rocks[i][j] == 'O':
                total_weight += max_w - i
    return total_weight


def roll_rock_north(rocks, i, j):
    while i > 0:
        if rocks[i-1][j] == '.':
            rocks[i-1][j] = 'O'
            rocks[i][j] = '.'
        else:
            break
        i -= 1


def north_iterator(rocks):
    for i in range(len(rocks)):
        for j in range(len(rocks[i])):
            yield i, j


def roll_rock_east(rocks, i, j):
    while j < len(rocks[i]) - 1:
        if rocks[i][j+1] == '.':
            rocks[i][j+1] = 'O'
            rocks[i][j] = '.'
        else:
            break
        j += 1


def east_iterator(rocks):
    for i in range(len(rocks)):
        for j in list(range(len(rocks[i])))[::-1]:
            yield i, j


def roll_rock_south(rocks, i, j):
    while i < len(rocks) - 1:
        if rocks[i+1][j] == '.':
            rocks[i+1][j] = 'O'
            rocks[i][j] = '.'
        else:
            break
        i += 1


def south_iterator(rocks):
    for i in list(range(len(rocks)))[::-1]:
        for j in range(len(rocks)):
            yield i, j


def roll_rock_west(rocks, i, j):
    while j > 0:
        if rocks[i][j-1] == '.':
            rocks[i][j-1] = 'O'
            rocks[i][j] = '.'
        else:
            break
        j -= 1


def west_iterator(rocks):
    for i in range(len(rocks)):
        for j in range(len(rocks[i])):
            yield i, j


def roll_rocks(rocks, roll_function, rock_iterator):
    # Start top left, row by row
    for i, j, in rock_iterator(rocks):
        if rocks[i][j] == 'O':
            roll_function(rocks, i, j)


def part_one():
    rocks = read_rocks()
    roll_rocks(rocks, roll_rock_north, north_iterator)
    result = calculate_weight_north(rocks)
    print(f'Part 1: {result}.')


def cycle_rocks(rocks):
    roll_rocks(rocks, roll_rock_north, north_iterator)
    roll_rocks(rocks, roll_rock_west, west_iterator)
    roll_rocks(rocks, roll_rock_south, south_iterator)
    roll_rocks(rocks, roll_rock_east, east_iterator)


def hashable(list):
    return tuple([tuple(row) for row in list])


def get_cycle(rocks, cycles):
    seen = {hashable(rocks): 0}
    for i in range(1, cycles):
        cycle_rocks(rocks)
        h = hashable(rocks)
        if h in seen:
            return seen.get(h), i, {v: k for k, v in seen.items()}
        else:
            seen[h] = i


def part_two():
    rocks = read_rocks()

    cycles = 1000000000
    i, j, configs = get_cycle(rocks, cycles)
    final_config = (cycles - i) % (j - i) + i
    weight = calculate_weight_north(configs.get(final_config))
    print(f'Part 2: {weight}.')


if __name__ == '__main__':
    part_one()
    part_two()
