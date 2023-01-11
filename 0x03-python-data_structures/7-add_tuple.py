#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0,0)
    new_tup = tuple(map(lambda a, b: a + b, tuple_a, tuple_b))[:2]
    return new_tup
