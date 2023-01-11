#!/usr/bin/python3
def element_at(my_list, idx):
    if len(my_list) < idx - 1:
        return None
    elif idx < 1:
        return None
    else:
        return ("{:d}".format(my_list[idx]))
