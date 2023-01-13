#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for i in matrix:
        a = list(map(lambda a: a**2, i))
        res.append(a)
    return res
