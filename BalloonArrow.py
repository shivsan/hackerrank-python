# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
from typing import List, Tuple


class Solution:
    def getOverLap(self, overLap: Tuple[int, int], pointsOfVerticalContour: Tuple[int, int]):
        left = max(overLap[0], pointsOfVerticalContour[0])
        right = min(overLap[1], pointsOfVerticalContour[1])

        if left > right:
            return None

        return [left, right]

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        arrows = 1

        firstArrowEnd = points[0][1]
        for s, e in points:
            if s > firstArrowEnd:
                arrows += 1
                firstArrowEnd = e
        return arrows
