from unittest import TestCase
from SchedulingJobs import Solution


class TestSolution(TestCase):
    def test_job_scheduling(self):
        self.assertEquals(Solution().jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]), 120)
        self.assertEquals(Solution().jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]), 150)
