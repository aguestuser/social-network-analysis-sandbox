import numpy as np


def parse_adjacency_matrices(incidence_matrix):
    return {
        'row': row_adjacencies(incidence_matrix),
        'col': col_adjacencies(incidence_matrix)
    }


def row_adjacencies(incidence_matrix):
    row_count = len(incidence_matrix)
    acc = np.zeros((row_count, row_count), dtype=int)
    for i in range(row_count):
        for j in range(row_count):
            if i != j:  # else leave it as 0
                acc[i][j] = count_common_values(incidence_matrix[i],
                                                incidence_matrix[j])
    return acc


def col_adjacencies(incidence_matrix):
    col_count = len(incidence_matrix[0])
    acc = np.zeros((col_count, col_count), dtype=int)
    for i in range(col_count):
        for j in range(col_count):
            if i != j:
                acc[i][j] = count_common_values(
                    column_from_idx(i, incidence_matrix),
                    column_from_idx(j, incidence_matrix)
                )
    return acc


# helpers


def column_from_idx(idx, matrix):
    return [row[idx] for row in matrix]


def count_common_values(row1, row2):
    # TODO: use bit-wise opeators?
    return sum([1 for x, y in zip(row1, row2) if x + y == 2])
