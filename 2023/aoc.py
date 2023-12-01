def read_file(filename):
    with open(filename) as f:
        return f.read()

def read_lines(filename):
    return read_file(filename).split('\n')
