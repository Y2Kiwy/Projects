import numpy

chessboard: list[list[int]] = [[6, 1, 7, 2, 5, 3, 0, 4],
                               [3, 2, 5, 4, 6, 7, 0, 1],
                               [1, 7, 2, 3, 4, 0, 6, 5],
                               [3, 5, 7, 0, 6, 4, 2, 1],
                               [4, 7, 5, 9, 3, 2, 5, 0],
                               [0, 4, 6, 2, 3, 5, 1, 7],
                               [1, 3, 5, 1, 7, 0, 6, 2],
                               [2, 7, 6, 5, 6, 4, 1, 3]]


def get_diagonals(matrix: list[list[int]], row: int, col: int) -> tuple:

    diagonal: list[int] = []
    anti_diagonal: list[int] = []

    # Calcolo della diagonale
    if row < col:
        for r, c in zip(range(0, 8), range(col - row, 8)):
            diagonal.append(matrix[r][c])
    else:
        for r, c in zip(range(row - col, 8), range(0, 8)):
            diagonal.append(matrix[r][c])

    # Calcolo della anti-diagonale
    if row + col < 7:
        start_row = 0
        start_col = row + col
    else:
        start_row = row + col - 7
        start_col = 7

    while start_row < 8 and start_col >= 0:
        anti_diagonal.append(matrix[start_row][start_col])
        start_row += 1
        start_col -= 1

    return diagonal, anti_diagonal

print("Posizione: 0:0", get_diagonals(chessboard, 0, 0), "\n")
print("Posizione: 0:1", get_diagonals(chessboard, 0, 1), "\n")
print("Posizione: 0:2", get_diagonals(chessboard, 0, 2), "\n")
print("Posizione: 0:3", get_diagonals(chessboard, 0, 3), "\n")
print("Posizione: 0:4", get_diagonals(chessboard, 0, 4), "\n")
print("Posizione: 0:5", get_diagonals(chessboard, 0, 5), "\n")
print("Posizione: 0:6", get_diagonals(chessboard, 0, 6), "\n")
print("Posizione: 0:7", get_diagonals(chessboard, 0, 7), "\n")
print("Posizione: 1:0", get_diagonals(chessboard, 1, 0), "\n")
print("Posizione: 1:1", get_diagonals(chessboard, 1, 1), "\n")
print("Posizione: 1:2", get_diagonals(chessboard, 1, 2), "\n")
print("Posizione: 1:3", get_diagonals(chessboard, 1, 3), "\n")
print("Posizione: 1:4", get_diagonals(chessboard, 1, 4), "\n")
print("Posizione: 1:5", get_diagonals(chessboard, 1, 5), "\n")
print("Posizione: 1:6", get_diagonals(chessboard, 1, 6), "\n")
print("Posizione: 1:7", get_diagonals(chessboard, 1, 7), "\n")
print("Posizione: 2:0", get_diagonals(chessboard, 2, 0), "\n")
print("Posizione: 2:1", get_diagonals(chessboard, 2, 1), "\n")
print("Posizione: 2:2", get_diagonals(chessboard, 2, 2), "\n")
print("Posizione: 2:3", get_diagonals(chessboard, 2, 3), "\n")
print("Posizione: 2:4", get_diagonals(chessboard, 2, 4), "\n")
print("Posizione: 2:5", get_diagonals(chessboard, 2, 5), "\n")
print("Posizione: 2:6", get_diagonals(chessboard, 2, 6), "\n")
print("Posizione: 2:7", get_diagonals(chessboard, 2, 7), "\n")
print("Posizione: 3:0", get_diagonals(chessboard, 3, 0), "\n")
print("Posizione: 3:1", get_diagonals(chessboard, 3, 1), "\n")
print("Posizione: 3:2", get_diagonals(chessboard, 3, 2), "\n")
print("Posizione: 3:3", get_diagonals(chessboard, 3, 3), "\n")
print("Posizione: 3:4", get_diagonals(chessboard, 3, 4), "\n")
print("Posizione: 3:5", get_diagonals(chessboard, 3, 5), "\n")
print("Posizione: 3:6", get_diagonals(chessboard, 3, 6), "\n")
print("Posizione: 3:7", get_diagonals(chessboard, 3, 7), "\n")
print("Posizione: 4:0", get_diagonals(chessboard, 4, 0), "\n")
print("Posizione: 4:1", get_diagonals(chessboard, 4, 1), "\n")
print("Posizione: 4:2", get_diagonals(chessboard, 4, 2), "\n")
print("Posizione: 4:3", get_diagonals(chessboard, 4, 3), "\n")
print("Posizione: 4:4", get_diagonals(chessboard, 4, 4), "\n")
print("Posizione: 4:5", get_diagonals(chessboard, 4, 5), "\n")
print("Posizione: 4:6", get_diagonals(chessboard, 4, 6), "\n")
print("Posizione: 4:7", get_diagonals(chessboard, 4, 7), "\n")
print("Posizione: 5:0", get_diagonals(chessboard, 5, 0), "\n")
print("Posizione: 5:1", get_diagonals(chessboard, 5, 1), "\n")
print("Posizione: 5:2", get_diagonals(chessboard, 5, 2), "\n")
print("Posizione: 5:3", get_diagonals(chessboard, 5, 3), "\n")
print("Posizione: 5:4", get_diagonals(chessboard, 5, 4), "\n")
print("Posizione: 5:5", get_diagonals(chessboard, 5, 5), "\n")
print("Posizione: 5:6", get_diagonals(chessboard, 5, 6), "\n")
print("Posizione: 5:7", get_diagonals(chessboard, 5, 7), "\n")
print("Posizione: 6:0", get_diagonals(chessboard, 6, 0), "\n")
print("Posizione: 6:1", get_diagonals(chessboard, 6, 1), "\n")
print("Posizione: 6:2", get_diagonals(chessboard, 6, 2), "\n")
print("Posizione: 6:3", get_diagonals(chessboard, 6, 3), "\n")
print("Posizione: 6:4", get_diagonals(chessboard, 6, 4), "\n")
print("Posizione: 6:5", get_diagonals(chessboard, 6, 5), "\n")
print("Posizione: 6:6", get_diagonals(chessboard, 6, 6), "\n")
print("Posizione: 6:7", get_diagonals(chessboard, 6, 7), "\n")
print("Posizione: 7:0", get_diagonals(chessboard, 7, 0), "\n")
print("Posizione: 7:1", get_diagonals(chessboard, 7, 1), "\n")
print("Posizione: 7:2", get_diagonals(chessboard, 7, 2), "\n")
print("Posizione: 7:3", get_diagonals(chessboard, 7, 3), "\n")
print("Posizione: 7:4", get_diagonals(chessboard, 7, 4), "\n")
print("Posizione: 7:5", get_diagonals(chessboard, 7, 5), "\n")
print("Posizione: 7:6", get_diagonals(chessboard, 7, 6), "\n")
print("Posizione: 7:7", get_diagonals(chessboard, 7, 7), "\n")