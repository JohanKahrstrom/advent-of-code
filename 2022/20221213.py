from functools import cmp_to_key

from aoc import read_file


def read_packet_pairs(text):
    packets = []
    for line1, line2 in list(zip(text[:-1], text[1:]))[::3]:
        packets.append((eval(line1), eval(line2)))

    return packets


def read_packets(text):
    packets = []
    for line in text:
        if line != '':
            packets.append(eval(line))

    return packets


def compare(packet1, packet2):
    if isinstance(packet1, int) and isinstance(packet2, int):
        if packet1 < packet2:
            return -1
        elif packet1 == packet2:
            return 0
        else:
            return 1
    elif isinstance(packet1, int) and isinstance(packet2, list):
        return compare([packet1], packet2)
    elif isinstance(packet1, list) and isinstance(packet2, int):
        return compare(packet1, [packet2])
    elif isinstance(packet1, list) and isinstance(packet2, list):

        cutoff = min([len(packet1), len(packet2)])
        for i in range(cutoff):
            result = compare(packet1[i], packet2[i])
            if result != 0:
                return result
        if len(packet1) < len(packet2):
            return -1
        elif len(packet1) == len(packet2):
            return 0
        else:
            return 1
    else:
        raise Exception(f"Can't compare types {type(packet1), type(packet2)}")


if __name__ == '__main__':
    text = read_file('20221213.txt').splitlines()
    # Part 1
    count = 0
    for i, (packet1, packet2) in enumerate(read_packet_pairs(text)):
        if compare(packet1, packet2) == -1:
            count += i+1
    print(f'Part 1: {count}.')

    # Part 2
    divider_packet1 = [[2]]
    divider_packet2 = [[6]]
    sorted_packets = sorted(read_packets(text) + [divider_packet1] + [divider_packet2], key=cmp_to_key(compare))

    print(f'Part 2: {(sorted_packets.index(divider_packet1)+1) * (sorted_packets.index(divider_packet2)+1)}')
