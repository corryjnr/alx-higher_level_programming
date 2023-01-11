#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    test_res = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            test_res.append(True)
        else:
            test_res.append(False)
    return test_res
