from diagonals import get_diagonals
from random import randint

chessboard: list[list[int]] = [[0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0]]

coordinates: dict = {"0;0": 0, "0;1": 0, "0;2": 0, "0;3": 0, "0;4": 0, "0;5": 0, "0;6": 0, "0;7": 0,
                     "1;0": 0, "1;1": 0, "1;2": 0, "1;3": 0, "1;4": 0, "1;5": 0, "1;6": 0, "1;7": 0,
                     "2;0": 0, "2;1": 0, "2;2": 0, "2;3": 0, "2;4": 0, "2;5": 0, "2;6": 0, "2;7": 0,
                     "3;0": 0, "3;1": 0, "3;2": 0, "3;3": 0, "3;4": 0, "3;5": 0, "3;6": 0, "3;7": 0,
                     "4;0": 0, "4;1": 0, "4;2": 0, "4;3": 0, "4;4": 0, "4;5": 0, "4;6": 0, "4;7": 0,
                     "5;0": 0, "5;1": 0, "5;2": 0, "5;3": 0, "5;4": 0, "5;5": 0, "5;6": 0, "5;7": 0,
                     "6;0": 0, "6;1": 0, "6;2": 0, "6;3": 0, "6;4": 0, "6;5": 0, "6;6": 0, "6;7": 0,
                     "7;0": 0, "7;1": 0, "7;2": 0, "7;3": 0, "7;4": 0, "7;5": 0, "7;6": 0, "7;7": 0}

def check_position(chessboard: list[list[int]], row: int, col: int) -> bool:

    print() # Formatting

    # Check if the position given is the same row of another queen
    for c in range(len(chessboard)):
        if chessboard[row][c] == 1:
            print(f"Found queen in position ({row};{c}) while checking rows")
            return False

    print() # Formatting
        
    # Check if the position given is the same column of another queen
    for r in range(len(chessboard)):
        if chessboard[r][col] == 1:
            print(f"Found queen in position ({r};{col}) while checking columns")
            return False
        
    # Check if the position given is the same diagonal or anti-diagonal of another queen
    diagonal: list[int] = get_diagonals(chessboard, row, col)[0]
    anti_diagonal: list[int] = get_diagonals(chessboard, row, col)[1]

    if 1 in diagonal:
        print(f"Found queen while checking diagonal {diagonal}")
        return False
    
    elif 1 in anti_diagonal:
        print(f"Found queen in position while checking anti-diagonal {anti_diagonal}")
        return False
    
    return True
    

def place_queens(chessboard: list[list[int]], start_r: int = 0, coordinates = coordinates) -> list[list[int]]:

    chessboard_size: int = len(chessboard)

    solution: list[list[int]] = chessboard

    # For each rows (from given start row to the last row) randomly choose one possible column where to put the queen
    for r in range(start_r, chessboard_size):

        print("-------------------------------------------------------------------------------")

        row_valid_position: list[tuple[int]] = []

        for c in range(chessboard_size):
            print(f"Checking value in position ({r};{c})")

            for row in solution:
                for elem in row:
                    print(elem, end=" ")
                print()

            print(coordinates)

            if check_position(chessboard, r, c):
                print(f"Value in position ({r};{c}) -> VALID")

                row_valid_position.append((r, c))
        
        # If at least one possible position is been founded, randomly place the queen
        if row_valid_position:
            print()

            print(f"{len(row_valid_position)} possible position found -> {row_valid_position}")

            random_qeen_position: int = randint(0, len(row_valid_position) - 1)

            random_col: int = row_valid_position[random_qeen_position][1]

            if coordinates[f"{r};{random_col}"] == 0:

                solution[r][random_col] = 1

                coordinates[f"{r};{random_col}"] = +1

                print()

                print(f"Queen placed in position ({r};{random_col})")
        
        else:
            print(f"No possible positions found, removing queen from row {r - 1} and backtracking...")

            if r == 0:
                return place_queens(chessboard)
            else:
                for i in range(chessboard_size):
                    # Reset the positions in the current row
                    solution[r - 1][i] = 0
                return place_queens(solution, r - 1)


    return solution


solution: list[list[int]] = place_queens(chessboard)

for row in solution:
    for value in row:
        print(value, end=" ")
    print()
