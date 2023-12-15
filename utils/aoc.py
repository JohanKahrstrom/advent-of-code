def read_file(filename):
    with open(filename) as f:
        return f.read()


def read_lines(filename):
    return read_file(filename).split('\n')


def print_a(array):
    # Prints a 2-d array
    if not isinstance(array[0][0], int):
        for line in array:
            print(''.join(line))
    else:
        for line in array:
            print(''.join([str(c) for c in line]))
