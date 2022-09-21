def multiply_matrix(matrix_a, matrix_b):
    final = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    print("MATRIX A\n")
    for l in matrix_a:
        print(l)
    print()
    print("MATRIX B\n")
    for l in matrix_b:
        print(l)
    print()
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                final[i][j] += matrix_a[i][k] * matrix_b[k][j]
    print("MULTIPLICAÇÃO\n")
    for l in final:
        print(l)