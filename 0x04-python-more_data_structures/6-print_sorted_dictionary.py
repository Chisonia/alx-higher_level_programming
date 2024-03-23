#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    if a_dictionary:
        for a, b in a_dictionary.items():
            keys.append(a)

    keys.sort()
    for key in keys:
        print("{}:{}".format(key, a_dictionary[key]))
