def get_matrix(n, m, value):
    matrix = []
    if m == 0:
        return matrix
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

print(get_matrix(5, 2, "x"))