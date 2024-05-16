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
                                [1, 3, 5, 1, 7, 0, 6, 2],
                                [2, 7, 6, 5, 0, 4, 1, 3]]


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