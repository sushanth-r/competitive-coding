def spiralTraverse(array):
    rows = len(array)
    columns = len(array[0])
    output = list()
    visited_matrix = list()
    for row in range(rows):
        new_column = [False for column in range(columns)]
        visited_matrix.append(new_column)
    all_elements_visited = False
    direction = "E"
    i, j = 0, 0
    while not all_elements_visited and rows > i > -1 and columns > j > -1:
        if not visited_matrix[i][j]:
            visited_matrix[i][j] = True
            output.append(array[i][j])
        else:
            all_elements_visited = True
        is_next_element_invalid, a, b = get_next_element_details(direction, visited_matrix, i, j, rows, columns)
        if is_next_element_invalid:
            direction = change_direction(direction)
        flag, i, j = get_next_element_details(direction, visited_matrix, i, j, rows, columns)
    return output


def get_next_element_details(direction: str, visited_matrix: list, i: int, j: int, rows: int, columns: int):
    if direction == "E":
        j += 1
    elif direction == "S":
        i += 1
    elif direction == "W":
        j -= 1
    else:
        i -= 1
    if i == rows:
        return True, i - 1, j - 1
    if i == -1:
        return True, i + 1, j + 1
    if j == columns:
        return True, i + 1, j - 1
    if j == -1:
        return True, i - 1, j + 1
    return visited_matrix[i][j], i, j


def change_direction(direction: str):
    if direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"
    else:
        return "E"


class SpiralTraverse:
    array = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ]
    print(spiralTraverse(array))
