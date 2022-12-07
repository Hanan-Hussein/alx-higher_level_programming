#!/usr/bin/python3
def square(n):
    return n * n


def square_matrix_simple(matrix=[]):
    new = [*matrix]
    for i in range(len(new)):
        for j in range(len(new[i])):
            new[i][j] = square(new[i][j])
    return new
