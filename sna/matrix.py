import numpy as np


def row_adjacencies(inc_matrix):
    return adjacencies(inc_matrix)


def col_adjacencies(inc_matrix):
    return adjacencies(inc_matrix.T)


def adjacencies(A_inc):
    """
    taking dot product of inc. matrix and its transpose yields adj. matrix
    b/c: multiplying matrix w/ transpose:
        === summing product of ith element in each row
            w/ ith element of every other row
        === counting common values btw/ each row and every other row
    subtracting diagonal removes cycles (ie: product of row and itself)
    """
    product = np.dot(A_inc, A_inc.T)
    return product - np.diag(np.diag(product))
