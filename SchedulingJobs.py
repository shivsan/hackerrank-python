# https://leetcode.com/problems/maximum-profit-in-job-scheduling/solution/
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        indexes = list(range(len(startTime)))
        indexes.sort(key=lambda i: startTime[i])

        return self.jobSchedulingRec(startTime, endTime, profit, indexes, 0, 0)

    def jobSchedulingRec(self,
                         startTime: List[int],
                         endTime: List[int],
                         profit: List[int],
                         indexes: List[int],
                         nextJobIndex: int,
                         lastJobEndTime: int) -> int:
        if nextJobIndex >= len(indexes):
            return 0

        if lastJobEndTime > startTime[nextJobIndex]: # Skip if schedule of next job overlaps with last job's schedule
            return self.jobSchedulingRec(startTime, endTime, profit, indexes, nextJobIndex + 1, lastJobEndTime)

        return max(self.jobSchedulingRec(startTime, endTime, profit, indexes, nextJobIndex + 1, endTime[nextJobIndex]) + profit[nextJobIndex],  # pick
                   self.jobSchedulingRec(startTime, endTime, profit, indexes, nextJobIndex + 1, lastJobEndTime))  # skip
