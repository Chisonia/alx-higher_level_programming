#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumint = 0
    for num in range(1, len(argv)):
        sumint += int(argv[num])
    print("{}".format(sumint))
