from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(u, v):
            parent_u, parent_v = find(u), find(v)
            if parent_u != parent_v:
                parent[parent_v] = parent_u

        for i, j in edges:
            union(i, j)
        return len(set(find(i) for i in range(n)))


class NumberOfConnectedComponentsInUndirectedGraph:
    n = 5
    edges = [[0,1],[1,2],[3,4]]
    x = Solution().countComponents(n, edges)
    print(x)
