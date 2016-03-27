def naive_matrix_multiplication(a, b):
    m = len(a)
    n = len(a[0])
    o = len(b)
    p = len(b[0])
    if n != o:
        raise ValueError('The number of columns in a must be equal to number of rows in b')
    result = []
    for i in range(m):
        result.append([0] * p)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result
