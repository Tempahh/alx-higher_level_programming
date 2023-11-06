#!/usr/bin/python3

def max_integer(my_list=[]):
    max_num = 0
    for nums in range(len(my_list)):
        if max_num <= my_list[nums]:
            max_num =my_list[nums]
    return max_num