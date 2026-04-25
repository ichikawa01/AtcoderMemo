def rotate_right(matrix):
    return [list(row) for row in zip(*matrix[::-1])]