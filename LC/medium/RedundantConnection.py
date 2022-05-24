import collections
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]

        def find(node):
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return False

            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]

            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge


class RedundantConnection:
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    x = Solution().findRedundantConnection(edges)
    print(x)
