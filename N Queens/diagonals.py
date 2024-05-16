def get_diagonals(matrix: list[list[int]], row: int, col: int) -> tuple[list[int]]:

    diagonal: list[int] = []
    anti_diagonal: list[int] = []

    matrix_size: int = len(matrix)

    # Calcolo della diagonale
    if row < col:
        for r, c in zip(range(0, matrix_size), range(col - row, matrix_size)):
            diagonal.append(matrix[r][c])
    else:
        for r, c in zip(range(row - col, matrix_size), range(0, matrix_size)):
            diagonal.append(matrix[r][c])

    # Calcolo della anti-diagonale
    if row + col < 7:
        start_row = 0
        start_col = row + col
    else:
        start_row = row + col - 7
        start_col = 7

    while start_row < matrix_size and start_col >= 0:
        anti_diagonal.append(matrix[start_row][start_col])
        start_row += 1
        start_col -= 1

    return diagonal, anti_diagonal

# 64 Test for each chessboard possible diagonals and anti-diagonals
# chessboard: list[list[int]] = [[6, 1, 7, 2, 5, 3, 0, 4],
#                                [3, 2, 5, 4, 6, 7, 0, 1],
#                                [1, 7, 2, 3, 4, 0, 6, 5],
#                                [3, 5, 7, 0, 6, 4, 2, 1],
#                                [4, 7, 5, 9, 3, 2, 5, 0],
#                                [0, 4, 6, 2, 3, 5, 1, 7],
#                                [1, 3, 5, 1, 7, 0, 6, 2],
#                                [2, 7, 6, 5, 6, 4, 1, 3]]
# chessboard_size: int = len(chessboard)
# for i in range(chessboard_size):
#     for j in range(chessboard_size):
#         print("Posizione:", i, ":", j, get_diagonals(chessboard, i, j), "\n")
