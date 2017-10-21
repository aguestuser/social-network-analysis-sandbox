import numpy as np
import sna.matrix as m


inc_matrix = np.array([
        [1, 1, 1, 1, 0],
        [1, 1, 1, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1]])

row_adjacency_matrix = np.array([
    [0, 3, 3, 1],
    [3, 0, 2, 2],
    [3, 2, 0, 1],
    [1, 2, 1, 0]])

col_adjacency_matrix = np.array([
    [0, 2, 2, 1, 1],
    [2, 0, 3, 2, 1],
    [2, 3, 0, 2, 2],
    [1, 2, 2, 0, 0],
    [1, 1, 2, 0, 0]])


def test_row_adjacencies():
    assert (m.row_adjacencies(inc_matrix) == row_adjacency_matrix).all()


def test_col_adjacencies():
    assert (m.col_adjacencies(inc_matrix) == col_adjacency_matrix).all()
