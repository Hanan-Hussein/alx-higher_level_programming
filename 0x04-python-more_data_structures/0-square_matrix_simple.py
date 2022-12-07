#!/usr/bin/python3
def square(n):
    return n * n


def square_matrix_simple(matrix=[]):
    new = [*matrix]
    for i in range(len(new)):
        print(i)
        for j in range(len(new[i])):
            print(j)
            new[i][j] = square(new[i][j])
    return new
