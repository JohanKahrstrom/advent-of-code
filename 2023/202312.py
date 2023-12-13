import re

from sortedcontainers import SortedKeyList

from aoc import read_lines


def read_springs():
    lines = read_lines('202312.txt')

    result = []

    for line in lines:
        springs = line.split(' ')[0]
        numbers = [int(n) for n in line.split(' ')[1].split(',')]

        result.append((springs, numbers))

    return result


class SpringCounter:
    # Wrapping this in a class to make it easier not to worry about resetting the cache

    def __init__(self):
        self.cache = {}

    def count_springs_cache(self, springs, numbers):
        if (springs, numbers) not in self.cache:
            self.cache[(springs, numbers)] = self.count_springs(springs, numbers)
        return self.cache[(springs, numbers)]

    def count_springs(self, springs, numbers):
        if len(numbers) == 0:
            # There can't be any '#' left in the spring, as we're out of numbers
            if '#' in springs:
                return 0
            else:
                return 1
        elif len(springs) == 0:
            # By the above if statement len(numbers) > 0, we have numbers left but no room
            # to fill them in.
            return 0
        else:
            # Both len(numbers) > 0 and len(string) > 0.
            # There must be precisely 1 string of ?/# of length numbers[0], followed
            # by either a period, question mark, or the end of the spring.
            if not re.match(f'[.?]*([#?]){{{numbers[0]}}}([?]|[.]|$)', springs):
                return 0
            else:
                if springs[0] == '#':
                    # A connected piece must start here of the correct length,
                    # followed by either the end of the string, a question mark or a period.:
                    if re.match(fr'([#?]){{{numbers[0]}}}([?]|[.]|$)', springs):
                        return self.count_springs_cache(springs[numbers[0]+1:], numbers[1:])
                    else:
                        return 0
                else:  # If springs[0] == '?':
                    count = 0
                    if re.match(fr'([#?]){{{numbers[0]}}}([?]|[.]|$)', springs):
                        count += self.count_springs_cache(springs[numbers[0]+1:], numbers[1:])
                    count += self.count_springs_cache(springs[1:], numbers)
                    return count


def part_one():
    springs_and_numbers = read_springs()

    result = 0
    for springs, numbers in springs_and_numbers:
        count = count_springs(springs, numbers)
        result += count
        print(count, springs, numbers)

    print(f'Part 1: {result}')


def part_two():
    springs_and_numbers = read_springs()

    result = 0
    for i, (springs, numbers) in enumerate(springs_and_numbers):
        springs = springs + '?' + springs + '?' + springs + '?' + springs + '?' + springs
        numbers = numbers * 5
        count = SpringCounter().count_springs(springs, tuple(numbers))
        result += count

    print(f'Part 2: {result}')


if __name__ == '__main__':
    part_two()
