from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def greater(a, b):
    if a > b:
        return a
    return b

print(reduce(greater, l))