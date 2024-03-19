#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    function_names = dir()
    for i in range(0, len(function_names)):
        if function_names[i][:2] != "__":
            print("{:s}".format(function_name[i]))
