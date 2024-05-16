import numpy as np

chessboard: list[list[int]] = [[0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0]]

chessboard2: list[list[int]] = [[0, 1, 2, 3, 4, 5, 6, 7],
                                [0, 1, 2, 3, 4, 5, 6, 7],
                                [0, 1, 2, 3, 4, 5, 6, 7],
                                [0, 1, 2, 3, 4, 5, 6, 7],
                                [0, 1, 2, 3, 4, 5, 6, 7],
                                [0, 1, 2, 3, 4, 5, 6, 7],
                                [0, 1, 2, 3, 4, 5, 6, 7],
                                [0, 1, 2, 3, 4, 5, 6, 7]]

chessboard3: list[list[int]] = [[6, 1, 7, 2, 5, 3, 0, 4],
                                [3, 2, 5, 4, 6, 7, 0, 1],
                                [1, 7, 2, 3, 4, 0, 6, 5],
                                [3, 5, 7, 0, 6, 4, 2, 1],
                                [4, 7, 5, 0, 3, 2, 5, 0],
                                [0, 4, 6, 2, 3, 5, 1, 7],
                                [1, 3, 9, 1, 7, 0, 6, 2],
                                [2, 7, 6, 5, 0, 4, 1, 3]]

def get_diagonals(matrix: list[list[int]], row: int, col: int) -> tuple[list[int]]:

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


def check_position(chessboard: list[list[int]], row: int, col: int) -> bool:

    print()

    # Check if the position given is the same row of another queen
    for c in range(len(chessboard)):
        if chessboard[row][c] == 1:
            print(f"Found queen in position ({row};{c}) while checking rows")
            return False

    print()
        
    # Check if the position given is the same column of another queen
    for r in range(len(chessboard)):
        if chessboard[r][col] == 1:
            print(f"Found queen in position ({r};{col}) while checking columns")
            return False
        
    diagonal: list[int] = get_diagonals(chessboard, row, col)[0]
    anti_diagonal: list[int] = get_diagonals(chessboard, row, col)[1]

    if 1 in diagonal:
        print(f"Found queen while checking diagonal {diagonal}")
        return False
    elif 1 in anti_diagonal:
        print(f"Found queen in position while checking anti-diagonal {anti_diagonal}")
        return False
    
    return True
    
