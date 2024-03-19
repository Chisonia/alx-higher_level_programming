#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    function_names = dir()
    for fun in range(len(function_names)):
        if function_names[fun][:2] != "__":
            print("{:s}".format(function_name[fun]))
