from itertools import chain, combinations

import networkx as nx

from aoc import read_lines


def read_valves():
    lines = read_lines('20221216.txt')

    valve_map = dict()
    tunnel_map = dict()

    for line in lines:
        valve_name = line.split()[1]
        valve_flow_rate = int(line.split('=')[1].split(';')[0])

        valve_map[valve_name] = valve_flow_rate
        tunnel_map[valve_name] = line.split(';')[1].replace(',', ' ').split()[4:]

    return valve_map, tunnel_map


def get_distances(tunnel_map):
    G = nx.Graph()

    for source, targets in tunnel_map.items():
        for target in targets:
            G.add_edge(source, target)

    result = dict()

    for source, targets in nx.all_pairs_dijkstra_path(G):
        result[source] = dict()
        for target, path in targets.items():
            result[source][target] = len(path) - 1

    return result


def get_potential_pressure_left(node, distances, t, valve_map, relevant_nodes):
    total_pressure = 0
    for target in relevant_nodes:
        distance = distances[node][target]
        time_left = max([t - distance - 1, 0])
        total_pressure += valve_map[target] * time_left
    return total_pressure


def search_paths(cum_pressure, current_pressure, current_node, t, relevant_nodes, valve_map, distances, previous_max):
    result = previous_max
    if len(relevant_nodes) == 0:
        cum_pressure = cum_pressure + current_pressure * t
        return max([cum_pressure, previous_max])

    for i in range(len(relevant_nodes)):
        target = relevant_nodes[i]
        distance = distances[current_node][target]
        time_left = t - distance - 1
        if time_left < 0:
            total_pressure = cum_pressure + current_pressure * t
            if total_pressure > result:
                result = total_pressure
            continue

        new_cum_pressure = cum_pressure + current_pressure * (distance + 1)
        new_current_pressure = current_pressure + valve_map[target]
        new_relevant_nodes = relevant_nodes[:i] + relevant_nodes[i+1:]

        # possible_max = (
        #     new_cum_pressure +
        #     get_potential_pressure_left(target, distances, t - distance - 1, valve_map, new_relevant_nodes) +
        #     new_current_pressure * time_left
        # )
        #
        # if possible_max < result:
        #     continue

        new_pressure = search_paths(new_cum_pressure, new_current_pressure, target, t - distance - 1, new_relevant_nodes, valve_map, distances, previous_max)

        if new_pressure > result:
            result = new_pressure

    return result


def part_one():
    valve_map, tunnel_map = read_valves()
    distances = get_distances(tunnel_map)

    t = 30
    current_node = 'AA'

    relevant = {valve: pressure for valve, pressure in valve_map.items() if pressure > 0}
    relevant_nodes = list(relevant.keys())

    max_value = search_paths(0, 0, current_node, t, relevant_nodes, valve_map, distances, 0)
    print(max_value)


def powerset(iterable):
    # Source: https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
    s = list(iterable)
    return chain.from_iterable(combinations(iterable, r) for r in range(len(s)+1))


def part_two():
    valve_map, tunnel_map = read_valves()
    distances = get_distances(tunnel_map)

    t = 26
    current_node = 'AA'

    max_value = 0
    relevant_nodes = set([valve for valve, pressure in valve_map.items() if pressure > 0])

    for set_a in powerset(relevant_nodes):
        set_a = sorted(list(set_a))
        set_b = sorted(list(relevant_nodes.difference(set_a)))

        value_a = search_paths(0, 0, current_node, t, set_a, valve_map, distances, 0)
        value_b = search_paths(0, 0, current_node, t, set_b, valve_map, distances, 0)

        value = value_a + value_b
        if value > max_value:
            max_value = value

    print(f'Part two: {max_value}')


if __name__ == '__main__':
    part_two()