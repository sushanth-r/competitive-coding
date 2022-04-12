def riverSizes(matrix):
    result = []
    visited = [[False for i in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            traverseNodes(i, j, matrix, result, visited)
    return result


def traverseNodes(i, j, matrix, result, visited):
    nodes = [[i, j]]
    current_river_size = 0
    while len(nodes) > 0:
        node = nodes.pop()
        x, y = node[0], node[1]
        if visited[x][y]:
            continue
        visited[x][y] = True
        if matrix[x][y] == 0:
            continue
        current_river_size += 1
        neighbour_nodes = get_neighbour_nodes(x, y, matrix)
        nodes += neighbour_nodes
    if current_river_size > 0:
        result.append(current_river_size)


def get_neighbour_nodes(i, j, matrix):
    nodes = []
    if i > 0:
        nodes.append([i - 1, j])
    if i < len(matrix) - 1:
        nodes.append([i + 1, j])
    if j > 0:
        nodes.append([i, j - 1])
    if j < len(matrix[0]) - 1:
        nodes.append([i, j + 1])
    return nodes


class RiverSizes:
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
    print(riverSizes(matrix))
