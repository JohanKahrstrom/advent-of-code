from collections import deque

from aoc import read_lines


def print_a(lines):
    print('-' * len(lines[0]))
    for line in lines:
        print(line)
    print('-' * len(lines[0]))


def find_start(lines):
    for i, line in  enumerate(lines):
        if 'S' in line:
            return line.index('S'), i


def read_pipes():
    lines = read_lines('202310.txt')
    start = find_start(lines)

    def pipes(x, y):
        # Helper function so we don't need to worry about checking outside the 'map'
        if x < 0:
            return '.'
        elif y < 0:
            return '.'
        elif x >= len(lines[0]):
            return '.'
        elif y >= len(lines):
            return '.'
        else:
            return lines[y][x]

    return start, lines, pipes


neighbour_map = {
    '|': lambda x, y: [(x, y-1), (x, y+1)],
    '-': lambda x, y: [(x-1, y), (x+1, y)],
    'L': lambda x, y: [(x, y-1), (x+1, y)],
    'J': lambda x, y: [(x, y-1), (x-1, y)],
    '7': lambda x, y: [(x-1, y), (x, y+1)],
    'F': lambda x, y: [(x, y+1), (x+1, y)],
    '.': lambda x, y: []
}


def get_neighbours(x, y, lines):
    return neighbour_map[lines[y][x]](x, y)


def get_start_neighbours(x, y, lines):
    neighbours = []
    if (x, y) in get_neighbours(x, y-1, lines):
        neighbours.append((x, y-1))
    if (x, y) in get_neighbours(x, y+1, lines):
        neighbours.append((x, y+1))
    if (x, y) in get_neighbours(x-1, y, lines):
        neighbours.append((x-1, y))
    if (x, y) in get_neighbours(x+1, y, lines):
        neighbours.append((x+1, y))

    return neighbours[0], neighbours[1]


def find_path(start, lines):
    lengths = {start: 0}
    path = deque([start])

    l, r = (start, start)
    ll, rr = get_start_neighbours(start[0], start[1], lines)
    while ll is not None and rr is not None:
        if ll is not None and ll not in lengths:
            path.appendleft(ll)
            lengths[ll] = lengths[l] + 1
            l = ll
            next_l = [node for node in get_neighbours(l[0], l[1], lines) if node not in lengths]
            if len(next_l) == 0:
                ll = None
            else:
                ll = next_l[0]
        if rr is not None and rr not in lengths:
            path.append(rr)
            lengths[rr] = lengths[r] + 1
            r = rr
            next_r = [node for node in get_neighbours(r[0], r[1], lines) if node not in lengths]
            if len(next_r) == 0:
                rr = None
            else:
                rr = next_r[0]

    return lengths, path


def part_one():
    start, lines, pipes = read_pipes()

    lengths, path = find_path(start, lines)

    print(f'Part 1: {max(lengths.values())}')


def get_quadrant(x, y):
    if x >= 0 and y >= 0:
        return 1
    elif x < 0 and y >= 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


def winding(x, y, path):
    quadrants = []

    for point in path:
        quadrant = get_quadrant(point[0] - x, point[1] - y)
        if len(quadrants) >= 1 and quadrants[-1] == quadrant:
            pass
        elif len(quadrants) >= 2 and quadrants[-2] == quadrant:
            quadrants.pop()
        else:
            quadrants.append(quadrant)

    if len(quadrants) // 4 > 0:
        return 'I'
    else:
        return 'O'


def part_two():
    start, lines, pipes = read_pipes()
    lengths, path = find_path(start, lines)

    fill = []
    for line in lines:
        fill.append([' '] * len(line))

    for (x, y) in path:
        fill[y][x] = 'P'

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if fill[y][x] != 'P':
                fill[y][x] = winding(x, y, path)

    inside = [
        point
        for line in fill
        for point in line
        if point == 'I'
    ]

    print(f'Part 2: {len(inside)}')


if __name__ == '__main__':
    part_two()
