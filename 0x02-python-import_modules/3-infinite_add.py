#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv);
    summ = 0
    for i in range(1, length):
        summ += int(argv[i])
    print("{:d}".format(summ))
