from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = len(board)
    cols = len(board[0])
    for i in range(0, 9):
        if not is_row_valid(i, board):
            return False
        if not is_column_valid(i, board):
            return False
        if i % 3 == 0:
            for j in range(0, 9, 3):
                if not is_grid_valid(i, j, board):
                    return False
    return True


def is_row_valid(row, board):
    current_row = board[row]
    non_empty_elements = []
    for element in current_row:
        if element != ".":
            non_empty_elements.append(element)
    return len(non_empty_elements) == len(set(non_empty_elements))


def is_column_valid(column, board):
    non_empty_elements = []
    for i, row in enumerate(board):
        element = board[i][column]
        if element != ".":
            non_empty_elements.append(element)
    return len(non_empty_elements) == len(set(non_empty_elements))


def is_grid_valid(row, col, board):
    non_empty_elements = []
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            element = board[i][j]
            if element != ".":
                non_empty_elements.append(element)
    return len(non_empty_elements) == len(set(non_empty_elements))


class ValidSudoku:
    board = [[".",".",".",".","5",".",".","1","."],
             [".","4",".","3",".",".",".",".","."],
             [".",".",".",".",".","3",".",".","1"],
             ["8",".",".",".",".",".",".","2","."],
             [".",".","2",".","7",".",".",".","."],
             [".","1","5",".",".",".",".",".","."],
             [".",".",".",".",".","2",".",".","."],
             [".","2",".","9",".",".",".",".","."],
             [".",".","4",".",".",".",".",".","."]]
    print(isValidSudoku(board))
