# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

import numpy
import scipy


def get_neighbors(matrix, row, col):
    neighbors = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        r = row + dr
        c = col + dc

        if 0 <= r < num_rows and 0 <= c < num_cols:
            neighbors.append((r, c))

    return neighbors


n = get_number()
m = get_number()
elevations = numpy.zeros((n, m))
for i in range(n):
    for j in range(m):
        elevations[i][j] = get_number()

water = numpy.ones((n, m))
max_el = numpy.max(elevations)

changed = True
while changed:
    changed = False
    for i in range(n):
        for j in range(m):
            if water[i][j] == 0:
                continue
            ns = get_neighbors(elevations, i, j)
            lower_ns = []
            for ne in ns:
                if elevations[i][j] > elevations[ne[0]][ne[1]]:
                    lower_ns.append(ne)
            if len(lower_ns) > 0:
                for ne in lower_ns:
                    water[ne[0]][ne[1]] += water[i][j] / len(lower_ns)
                    changed = True
                water[i][j] = 0

print(numpy.max(water))