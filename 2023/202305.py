from utils.aoc import read_lines


def read_map(i, lines):
    # Skip header
    i += 1

    pairs = []
    while i < len(lines) and lines[i] != '':
        numbers = [int(n) for n in lines[i].split(' ')]
        # Pairs contain start, end, offset
        # if start <= n <= end then return n + offset
        # 10 3 4 -> (3, 6, 7)
        pairs.append((numbers[1], numbers[1] + numbers[2] - 1, numbers[0] - numbers[1]))

        i += 1

    # Skip empty line:
    i += 1

    def resource_map(n):
        for start, end, offset in pairs:
            if start <= n <= end:
                return n + offset
        return n

    return i, resource_map, pairs


def read_seeds_and_maps():
    lines = read_lines('202305.txt')

    seeds = [int(n) for n in lines[0].split(':')[1].split(' ') if n != '']

    i = 2

    maps = []
    while i < len(lines):
        i, resource_map, pairs = read_map(i, lines)
        maps.append((resource_map, pairs))

    return seeds, maps


def part_one():
    seeds, maps = read_seeds_and_maps()

    seed_results = []

    for seed in seeds:
        s = seed
        for resource_map, _ in maps:
            s = resource_map(s)
        seed_results.append(s)

    print(f'Part 1: {min(seed_results)}')


def shift_segment(pairs, seed_start, seed_end):
    for shift_start, shift_end, shift_offset in pairs:
        if shift_start <= seed_start and seed_end <= shift_end:
            return (seed_start + shift_offset, seed_end + shift_offset)
    return (seed_start, seed_end)


def map_segments(seed_list, pairs):
    # Firs split the seed list into fine enough units that
    # each pair maps units a single way
    splits_1 = [(f - 0.5, t + 0.5) for f, t, _ in pairs]
    splits = sorted(list(set([point for split in splits_1 for point in split])))

    for split in splits:
        split_seed_list = []
        for seed_start, seed_end in seed_list:
            if seed_start < split < seed_end:
                split_seed_list += [(seed_start, split - 0.5), (split + 0.5, seed_end)]
            else:
                split_seed_list += [(seed_start, seed_end)]
        seed_list = split_seed_list

    # Now map each seed segment
    result = []
    for seed_start, seed_end in seed_list:
        result.append(shift_segment(pairs, seed_start, seed_end))

    return result


def part_two():
    seeds, maps = read_seeds_and_maps()

    mins = []

    for seed_start, seed_length in zip(seeds[0::2], seeds[1::2]):
        seed_end = seed_start + seed_length

        seed_list = [(seed_start, seed_end)]

        for _, pairs in maps:
            seed_list = map_segments(seed_list, pairs)

        mins.append(min([start for start, _ in seed_list]))

    print(min(mins))


if __name__ == '__main__':
    part_two()
