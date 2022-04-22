from queue import Queue


def minimumPassesOfMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    def get_negative_neighbours(x, y):
        nodes = []
        if x > 0 and matrix[x - 1][y] < 0:
            nodes.append([x - 1, y])
        if x < len(matrix) - 1 and matrix[x + 1][y] < 0:
            nodes.append([x + 1, y])
        if y > 0 and matrix[x][y - 1] < 0:
            nodes.append([x, y - 1])
        if y < len(matrix[0]) - 1 and matrix[x][y + 1] < 0:
            nodes.append([x, y + 1])
        return nodes

    flag = True
    result = 0
    positive_queue = Queue()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] > 0:
                positive_queue.put([i, j])
    while flag:
        transformed_queue = Queue()
        elements_transformed = 0
        while positive_queue.qsize() > 0:
            node = positive_queue.get()
            i, j = node[0], node[1]
            negative_neighbours = get_negative_neighbours(i, j)
            for neighbour in negative_neighbours:
                i, j = neighbour[0], neighbour[1]
                matrix[i][j] *= -1
                transformed_queue.put([i, j])
                elements_transformed += 1
        are_negative_elements_remaining = False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] < 0:
                    are_negative_elements_remaining = True
                    break
        if elements_transformed == 0 and are_negative_elements_remaining:
            return -1
        elif elements_transformed == 0:
            flag = False
            break
        result += 1
        while transformed_queue.qsize() > 0:
            positive_queue.put(transformed_queue.get())
    return result


class MinimumPassesOfMatrix:
    matrix = [
      [1, 0, 0, -2, -3],
      [-4, -5, -6, -2, -1],
      [0, 0, 0, 0, -1],
      [1, 2, 3, 0, 3]
    ]
    print(minimumPassesOfMatrix(matrix))
