# a simple parser for python. use get_number() and get_word() to read
from math import floor


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
num_it = get_number()

for it in range(num_it):
    v0 = get_number()
    v1 = get_number()
    numero_iterazioni = get_number()

    v6 = 1
    v9 = v0 + v1
    v10 = 0
    for count in range(1, numero_iterazioni + 1):
        v10 += v0
        v13 = v10

        v13 = v13 % v1
        while v13 > v1/2:
            v13 -= v1

        v13 = abs(v13)

        v17 = v13 * v6 - v9 * count

        if v17 < 0:
            v6 = count
            v9 = v13

    print(v6)