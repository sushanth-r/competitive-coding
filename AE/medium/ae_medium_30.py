def removeIslands(matrix):
    visited = [[False for i in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            traverseNodes(i, j, matrix, visited)
    return matrix


def traverseNodes(i, j, matrix, visited):
    nodes = [[i, j]]
    island_nodes = []
    is_island = True
    while len(nodes) > 0:
        node = nodes.pop()
        x = node[0]
        y = node[1]
        if visited[x][y]:
            continue
        visited[x][y] = True
        if matrix[x][y] == 0:
            continue
        if x == 0 or x == (len(matrix) - 1) or y == 0 or y == (len(matrix[0]) - 1):
            is_island = False
        else:
            island_nodes.append(node)
        neighbouring_nodes = getNeighbourNodes(x, y, matrix)
        nodes += neighbouring_nodes
    if is_island:
        for node in island_nodes:
            x, y = node[0], node[1]
            matrix[x][y] = 0


def getNeighbourNodes(i, j, matrix):
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


class RemoveIslands:
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]
    print(removeIslands(matrix))
