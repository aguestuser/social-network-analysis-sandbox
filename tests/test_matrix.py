import numpy as np
import sna


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


def test_parse_adjacency_matrices():
    result = sna.parse_adjacency_matrices(inc_matrix)
    expected = {
        'row': row_adjacency_matrix,
        'col': col_adjacency_matrix
    }
    for k, v in result.iteritems():
        assert (v == expected[k]).all()


def test_row_adjacencies():
    assert (sna.row_adjacencies(inc_matrix) == row_adjacency_matrix).all()


def test_col_adjacencies():
    assert (sna.col_adjacencies(inc_matrix) == col_adjacency_matrix).all()


def test_column_from_idx():
    matrix = [[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3]]
    assert sna.column_from_idx(1, matrix) == [2, 2, 2]


def test_count_common_values():
    r1 = [0, 1, 0]
    r2 = [0, 1, 1]
    assert sna.count_common_values(r1, r2) == 1
