class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def dfs(existing_node: Node):
            if existing_node in visited:
                return visited[existing_node]
            new_node = Node(existing_node.val)
            visited[existing_node] = new_node
            for neighbour in existing_node.neighbors:
                new_node.neighbors.append(dfs(neighbour))
            return new_node

        return dfs(node) if node else None


class CloneGraph:
    One = Node(1)
    Two = Node(2)
    Three = Node(3)
    One.neighbors = [Two, Three]
    x = Solution().cloneGraph(One)
    print(x)
