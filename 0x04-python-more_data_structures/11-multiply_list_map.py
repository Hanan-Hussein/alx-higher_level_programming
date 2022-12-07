#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mine_l = my_list.copy()
    return list(map(lambda i: i * number, mine_l))
