#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = list(map(list, matrix))
    for i in range(len(new)):
        for j in range(len(new[i])):
            new[i][j] = new[i][j] ** 2
    return new
