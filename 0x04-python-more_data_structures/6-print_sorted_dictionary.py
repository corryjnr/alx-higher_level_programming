#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    for i in a_dictionary:
        keys.append(i)
    keys.sort()
    for i in keys:
        print(f"{i:s}: {a_dictionary[i]}")
