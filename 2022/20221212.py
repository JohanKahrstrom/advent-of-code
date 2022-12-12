from collections import deque

import numpy as np

from aoc import read_file


def read_maze(filename):
    text = [
        [c for c in line]
        for line in read_file(filename).split('\n')
    ]
    start = (-1, -1)
    end = (-1, -1)

    for i, line in enumerate(text):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
                text[i][j] = 'a'
            if c == 'E':
                end = (i, j)
                text[i][j] = 'z'

    maze = np.array([
        [ord(c) - 97 for c in line]
        for line in text
    ])

    return maze, start, end


def inside_maze(node, maze):
    x, y = node
    if x < 0 or y < 0:
        return False
    elif x >= len(maze) or y >= len(maze[0]):
        return False
    else:
        return True


def climbable(node, neighbour, maze):
    return maze[neighbour] <= maze[node] + 1


def get_neighbours(node, maze):
    x, y = node
    neigbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    return [
        neighbour
        for neighbour in neigbours
        if inside_maze(neighbour, maze)
        and climbable(node, neighbour, maze)
    ]


def dijkstra(maze, start):
    cost = np.ones(maze.shape, dtype=int) * (100000)
    cost[start] = 0

    to_visit = deque([start])

    while len(to_visit) > 0:
        node = to_visit.popleft()
        for neighbour in get_neighbours(node, maze):
            if cost[neighbour] > cost[node] + 1:
                cost[neighbour] = cost[node] + 1
                to_visit.append(neighbour)

    return cost


if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)
    maze, start, end = read_maze('20221212.txt')
    # Part 1
    cost = dijkstra(maze, start)
    print(f'Part 1: {cost[end]}')

    # Part 2
    cost = dijkstra(-maze, end)
    print(f'Part 2: {(cost * (maze == 0) + (maze > 0) * 10000).min()}')
