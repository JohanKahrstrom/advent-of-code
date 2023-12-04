from collections import deque

import numpy as np

from aoc import read_lines


def read_cards():
    lines = read_lines('202304.txt')
    result = []

    for line in lines:
        card_number = int(line.split(':')[0].split(' ')[-1])
        winners = set([int(n) for n in line.split(':')[1].split('|')[0].split(' ') if n != ''])
        yours = set([int(n) for n in line.split(':')[1].split('|')[1].split(' ') if n != ''])

        result.append((card_number-1, winners, yours))

    return result


def get_matches(card: (int, set[int], set[int])):
    card_number, winners, yours = card
    return len([n for n in yours if n in winners])


def get_score(n):
    if n <= 0:
        return 0
    else:
        return 2 ** (n - 1)


def part_one():
    cards = read_cards()

    total_score = 0

    for card in cards:
        nr_matches = get_matches(card)
        total_score += get_score(nr_matches)

    print(f'Part 1: {total_score}')


def part_two():
    cards = read_cards()
    q = deque(cards)

    nr_cards = 0
    while len(q) > 0:
        nr_cards += 1
        card = q.popleft()

        card_number, _, _ = card
        matches = get_matches(card)
        for i in range(card_number + 1, card_number + 1 + matches):
            q.append(cards[i])

    print(f'Part 2: {nr_cards}')


def get_card_vectors(cards):
    dim = max([card_number for card_number, _, _ in cards]) + 1

    # Initially we have one of each card
    card_counts = np.ones(dim, dtype=int)

    # A card vector is a vector of how many cards of each number to add
    # for each card
    card_vectors = []
    for card in cards:
        card_vector = np.zeros(dim, dtype=int)
        card_number, _, _ = card
        matches = get_matches(card)
        for i in range(card_number + 1, card_number + 1 + matches):
            card_vector[i] = 1
        card_vectors.append(card_vector)

    return card_counts, card_vectors


def part_two_v2():
    cards = read_cards()
    card_counts, card_vectors = get_card_vectors(cards)

    for i in range(card_counts.shape[0]):
        card_counts += card_counts[i] * card_vectors[i]

    print(f'Part 2: {card_counts.sum()}')

if __name__ == '__main__':
    part_two_v2()
