from collections import Counter

from aoc import read_lines


def get_type(hand_string):
    c = Counter(hand_string)
    if c.most_common()[0][1] == 5:
        return 7
    if c.most_common()[0][1] == 4:
        return 6
    if len(c.values()) == 2:
        return 5
    if c.most_common()[0][1] == 3 and len(c.values()) == 3:
        return 4
    if c.most_common()[0][1] == 2 and len(c.values()) == 3:
        return 3
    if c.most_common()[0][1] == 2 and len(c.values()) == 4:
        return 2
    else:
        return 1


def parse_hand(line):
    hand_string = line.split()[0]
    bid = int(line.split()[1])

    hand_type = get_type(hand_string)

    high_map = str.maketrans({
        'T': 'A',
        'J': 'B',
        'Q': 'C',
        'K': 'D',
        'A': 'E'
    })

    clean_string = hand_string.translate(high_map)

    return hand_string, clean_string, hand_type, bid


def read_hands():
    lines = read_lines('202307.txt')

    hands = [parse_hand(hand) for hand in lines]

    return hands


def part_one():
    hands = read_hands()

    sorted_hands = sorted(
        hands,
        key=lambda hand: str(hand[2]) + hand[1],
    )
    total_winnings = sum([bid * (i+1) for (i, (_, _, _, bid)) in enumerate(sorted_hands)])

    print(f'Part 1: {total_winnings}')


def find_best_hand(hand):
    hand_string, clean_string, hand_type, bid = hand

    if 'J' not in hand_string:
        return hand

    best_hand, best_type = hand_string, hand_type
    for card in set(hand_string).difference({'J'}):
        joker_map = _map = str.maketrans({
            'J': card
        })

        new_hand = hand_string.translate(joker_map)
        new_type = get_type(new_hand)

        if new_type > best_type:
            best_hand, best_type = new_hand, new_type

    high_map = str.maketrans({
        'T': 'A',
        'J': '0',
        'Q': 'C',
        'K': 'D',
        'A': 'E'
    })

    best_clean_string = hand_string.translate(high_map)

    return best_hand, best_clean_string, best_type, bid


def part_two():
    hands = read_hands()

    best_hands = [find_best_hand(hand) for hand in hands]

    sorted_hands = sorted(
        best_hands,
        key=lambda hand: str(hand[2]) + hand[1],
    )

    total_winnings = sum([bid * (i+1) for (i, (_, _, _, bid)) in enumerate(sorted_hands)])

    print(f'Part 2: {total_winnings}')


if __name__ == '__main__':
    part_two()
