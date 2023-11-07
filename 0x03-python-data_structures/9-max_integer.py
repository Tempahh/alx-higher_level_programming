#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_num = my_list[0]
    for nums in range(len(my_list)):
        if max_num < my_list[nums]:
            max_num = my_list[nums]
    return max_num
