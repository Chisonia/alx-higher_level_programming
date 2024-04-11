#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number = 0
    for items in range(x):
        try:
            print("{:d}".format(my_list[items]), end='')
            number += 1
        except (ValuError, TypeErrror):
            pass
        print()
        return number
