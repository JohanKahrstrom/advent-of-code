from utils.aoc import read_lines


def read_sequence():
    return ''.join(read_lines('202315.txt')).split(',')


def calculate_hash(string):
    result = 0
    for c in string:
        result = ((result + ord(c)) * 17) % 256
    return result


def part_one():
    sequence = read_sequence()
    result = sum([calculate_hash(string) for string in sequence])

    print(f'Part 1: {result}.')


def get_operations(sequence):
    operations = []
    for instruction in sequence:
        if '-' in instruction:
            label = instruction.split("-")[0]
            box = calculate_hash(label)
            operations.append(("del", label, box, None))
        elif '=' in instruction:
            label = instruction.split("=")[0]
            box = calculate_hash(label)
            focal_strength = int(instruction.split("=")[1])
            operations.append(("add", label, box, focal_strength))

    return operations


def find_label(box, label):
    for i in range(len(box)):
        if box[i][0] == label:
            return i
    return -1


def calculate_focusing_power(boxes):
    focusing_power = 0
    for i, box in boxes.items():
        for j, (label, focal_strength) in enumerate(box):
            focusing_power += (i+1) * (j+1) * focal_strength

    return focusing_power


def part_two():
    operations = get_operations(read_sequence())
    boxes = {}
    for operation, label, box, focal_strength in operations:
        if operation == "del" and box in boxes:
            i = find_label(boxes[box], label)
            if i >= 0:
                del boxes[box][i]
        elif operation == "add":
            if box not in boxes:
                boxes[box] = [(label, focal_strength)]
            else:
                i = find_label(boxes[box], label)
                if i < 0:
                    boxes[box].append((label, focal_strength))
                else:
                    boxes[box][i] = (label, focal_strength)


    print(f'Part 2: {calculate_focusing_power(boxes)}.')


if __name__ == '__main__':
    part_one()
    part_two()
