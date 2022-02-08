# https://leetcode.com/problems/number-of-islands/

from typing import List, Tuple


class Solution:
    def __init__(self):
        self.numberOfIslands = 0

    def getNumberOfIslands(self, map: List[List[str]]) -> int:
        self.traverseAndMarkVisited(map)

        return self.numberOfIslands

    def traverseAndMarkVisited(self, map: List[List[str]]):
        m = len(map)  # rows
        n = len(map[0])  # columns

        for x in range(m):
            for y in range(n):
                # If land not visited, then count as new island
                if map[x][y] == "1":
                    map[x][y] = "0"
                    self.numberOfIslands += 1
                    self.depthFirstTraversalAndMarkingAsVisited(map, x, y)

    def depthFirstTraversalAndMarkingAsVisited(self, map: List[List[str]], x: int, y: int) -> bool:
        m = len(map)  # rows
        n = len(map[0])  # columns
        map[x][y] = "0"

        # Move across boundary if there is land and it is not visited
        # go up
        if x > 0 and map[x - 1][y] != "0":
            self.depthFirstTraversalAndMarkingAsVisited(map, x - 1, y)

        # go right
        if y < n - 1 and map[x][y + 1] != "0":
            self.depthFirstTraversalAndMarkingAsVisited(map, x, y + 1)

        # go down
        if x < m - 1 and map[x + 1][y] != "0":
            self.depthFirstTraversalAndMarkingAsVisited(map, x + 1, y)

        # go left
        if y > 0 and map[x][y - 1] != "0":
            self.depthFirstTraversalAndMarkingAsVisited(map, x, y - 1)
