import collections
from typing import List


class Solution:
    # Union Find
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        def union(i, j):
            pi, pj = find(i), find(j)
            if pi == pj:
                return False

            if rank[i] >= rank[j]:
                parent[pj] = pi
                rank[i] += rank[j]
            else:
                parent[pi] = pj
                rank[j] += rank[i]
            return True

        for x, y in edges:
            if not union(x, y):
                return False

        return len(set(find(i) for i in range(n))) == 1

    def validTreeDfs(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list)
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour in visited:
                    if neighbour == parent:
                        continue
                    return False
                if not dfs(neighbour, node):
                    return False
            return True

        return dfs(0, -2) and len(visited) == n

    def validTreeBfs(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list)
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        visited = set()

        def bfs(queue):
            while queue:
                node, parent = queue.popleft()
                if node in visited:
                    return False
                visited.add(node)
                for neighbour in adj_list[node]:
                    if neighbour in visited:
                        if neighbour == parent:
                            continue
                        return False
                    queue.append((neighbour, node))
            return True

        node_queue = collections.deque()
        node_queue.append((0, -2))
        return bfs(node_queue) and len(visited) == n


class GraphValidTree:
    n = 5
    edges = [[0,1],[0,2],[0,3],[1,4]]
    x = Solution().validTreeBfs(n, edges)
    print(x)
