import collections
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            u = edge[0]
            v = edge[1]

            if dsu.isConnected(u, v):
                return edge

            dsu.addEdge(u, v)


class DSU:
    def __init__(self):
        self.parents = collections.defaultdict(lambda: None)

    def findParent(self, x: int) -> int:
        while self.parents[x] is not None and self.parents[x] != x:
            x = self.parents[x]

        return self.parents[x]

    def isConnected(self, x, y) -> bool:
        return self.findParent(x) == self.findParent(y)

    def addEdge(self, u, v):
        parentU = self.findParent(u)
        parentV = self.findParent(v)

        if parentU is None and parentV is None:
            self.parents[u] = v
            self.parents[v] = v
            return

        if parentU is not None and parentV is not None:
            self.parents[parentV] = parentU
            return

        if parentU is None:
            self.parents[u] = v
        else:
            self.parents[v] = u


    def isConnected(self, u, v):
        parent = self.findParent(u)
        if parent is None:
            return False
        return parent == self.findParent(v)
