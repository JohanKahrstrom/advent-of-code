from itertools import cycle, count
import re
import math

import numpy as np

from aoc import read_lines


def read_map():
    lines = read_lines('202308.txt')

    instructions = cycle(lines[0])

    network = dict()
    for line in lines[2:]:
        match = re.match(r'(\w+) = \((\w+), (\w+)\)', line)
        node = match.group(1)
        left = match.group(2)
        right = match.group(3)
        network[node] = dict()
        network[node]['L'] = left
        network[node]['R'] = right

    return instructions, network


def part_one():
    instructions, network = read_map()
    _
    node = 'AAA'

    for i in count(start=1):
        direction = next(instructions)
        node = network[node][direction]
        if node == 'ZZZ':
            break

    print(f'Part 1: {i}')


def sgn(a):
    if a < 0:
        return -1
    else:
        return 1


def extended_euclid(a, b, c):
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    gcd = math.gcd(a, b)
    if c % gcd != 0:
        raise Exception(f'Only works if gcd(a, b) divides c ({c % gcd})')
    factor = c / gcd
    swapped = False
    if abs(a) < abs(b):
        swapped = True
        (a, b) = (b, a)
    r = [a, b]
    s = [1, 0]
    t = [0, 1]
    print(r)
    while r[-1] != 0:
        q = r[-2] // r[-1]
        r.append(r[-2] - q * r[-1])
        s.append(s[-2] - q * s[-1])
        t.append(t[-2] - q * t[-1])
        print(r)
        print(s)
        print(t)
    if swapped:
        return t[-2] * factor, s[-2] * factor
    else:
        return s[-2] * factor, t[-2] * factor


def part_two():
    a = 16697
    b = 20093
    c1 = 33394
    c2 = 40186
    c = c2 - c1
    gcd = math.gcd(a, b)
    print(gcd)
    print(math.gcd(a, b), math.gcd(a, c1), math.gcd())
    t1, t2 = extended_euclid(a, -b, c)
    print(c, t1 * a - t2 * b)
    print(a * t1 + c1)
    print(b * t2 + c2)
    r = 3
    s1 = t1 + r * b / math.gcd(a, -b)
    s2 = t2 + r * a / math.gcd(a, -b)

    print(c, s1 * a - s2 * b)
    print(a * s1 + c1)
    print(b * s2 + c2)

    print(a * b / math.gcd(a, -b))

    factor = a * b / math.gcd(a, b)
    u1 = (factor - c1) / a
    u2 = (factor - c2) / b
    print(a * u1 + c1)
    print(b * u2 + c2)

    instructions, network = read_map()

    nodes = sorted({node for node, _ in network.items() if node[-1] == 'A'})

    max_nodes_at_end = 0
    log_step = 10
    last_node_at_end = {}
    diff_at_end = {}
    recurrence = {}
    for i in count(start=1):
        direction = next(instructions)
        nodes = {network[node][direction] for node in nodes}

        nodes_at_end = {node for node in nodes if node[-1] == 'Z'}
        if len(nodes_at_end) == len(nodes):
            break
        if len(nodes_at_end) > max_nodes_at_end:
            max_nodes_at_end = len(nodes_at_end)
        if len(nodes_at_end) > 0:
            for n in nodes_at_end:
                l = last_node_at_end.get(n, [])
                if len(l) == 0:
                    prev_end = 0
                else:
                    prev_end = l[-1][0]
                diff = i - prev_end
                l.append((i, diff))
                last_node_at_end[n] = l

        if i % log_step == 0:
            log_step *= 10
            print(f'At {i} steps, max {max_nodes_at_end} nodes at end.')

        if i > 1000000:
            break
    print(nodes)
    print(last_node_at_end)
    print(recurrence)
    print(f'Part 2: {i}')
    test = [cycle_length for _, (_, cycle_length) in recurrence.items()]
    prod = 1
    for t in test:
        prod *= t
    print(int(math.lcm(*[cycle_length for _, (_, cycle_length) in recurrence.items()])))
    print(math.gcd(*[index for _, (index, _) in recurrence.items()]))
    print(283 * 2)


if __name__ == '__main__':
    part_two()
