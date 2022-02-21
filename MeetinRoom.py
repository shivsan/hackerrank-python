# https://leetcode.com/problems/meeting-rooms-ii/solution/
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        rooms = []
        heapq.heapify(rooms)
        heapq.heappush(rooms, intervals[0][1])

        for s, e in intervals[1:]:
            if rooms[0] < s:
                heapq.heappop(rooms)
            heapq.heappush(rooms, e)

        return len(rooms)

    def binarySearchGreaterThan(self, array: List[int], value: int) -> int:
        l, r = 0, len(array) - 1

        if value > array[-1]:
            return len(array)

        if value < array[0]:
            return -1

        while not (array[l] <= value < array[l + 1]):
            if value < array[int((l + r) / 2)]:
                r = int((l + r) / 2)
            elif value > array[int((l + r) / 2)]:
                l = int((l + r) / 2)
            else:
                return int((l + r) / 2)

        return l
