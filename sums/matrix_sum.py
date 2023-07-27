if __name__ == "__main__":
    row_size, col_size = list(map(int, input().split()))
    matrix_1 = []
    matrix_2 = []
    # Read first matrix
    for i in range(row_size):
        matrix_1.append(list(map(int, input().split())))
    for i in range(row_size):
        matrix_2.append(list(map(int, input().split())))

    for row in range(row_size):
        for col in range(col_size):
            matrix_1[row][col] += matrix_2[row][col]
        print(*matrix_1[row])