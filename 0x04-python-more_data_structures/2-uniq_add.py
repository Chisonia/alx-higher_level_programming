#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    if my_list:
        for num in my_list:
            my_set.add(num)
    return sum(my_set)
