# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
from typing import List, Tuple


class Solution:
    def getOverLap(self, overLap: Tuple[int, int], pointsOfVerticalContour: Tuple[int, int]):
        left = max(overLap[0], pointsOfVerticalContour[0])
        right = min(overLap[1], pointsOfVerticalContour[1])

        if left > right:
            return None

        return [left, right]

    def getMinimumArrowsRec(self, points: List[List[int]],
                            pointIndex: int,
                            overLap: Tuple[int, int],
                            memo: dict) -> int:
        if pointIndex >= len(points):
            return 0

        if memo.get(pointIndex) is not None:
            return memo[pointIndex]

        # If there is no overlap, then new arrow
        if overLap is None:
            overLap = [points[pointIndex][0], points[pointIndex][1]]
            result = self.getMinimumArrowsRec(points, pointIndex + 1, overLap, memo) + 1
            memo[pointIndex] = result
            return result

        if self.getOverLap(overLap, points[pointIndex]) is None:
            result = self.getMinimumArrowsRec(points, pointIndex + 1, None, memo) + 1
            memo[pointIndex] = result
            return result

        # If there is overlap, get the minimum of the options with picking the balloon or not
        result = min(self.getMinimumArrowsRec(points, pointIndex + 1, None, memo),  # skip
                     self.getMinimumArrowsRec(points, pointIndex + 1, self.getOverLap(overLap, points[pointIndex]),
                                              memo))  # Take
        memo[pointIndex] = result
        return result

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        memo = {}
        self.getMinimumArrowsRec(points, 0, None, memo)

        print(points)
        return memo.get(0)
