#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1;
    summ = 0
    if length == 0:
        print("{:d}".format(0));
    else:
        for i in range(1, length+1):
            summ += int(argv[i])
        print("{:d}".format(summ))
