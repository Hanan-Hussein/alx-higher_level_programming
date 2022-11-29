#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 64 and ord(i) < 91:
            print(i)
        elif ord(i) > 96 and ord(i) < 122:
            print(chr(ord(i) - 32))
        else:
            print(i)

