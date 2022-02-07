from unittest import TestCase

from BalloonArrow import Solution


class Test(TestCase):
    def test_get_minimum_arrows(self):
        solution = Solution()
        # self.assertEquals(solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]), 2)
        # self.assertEquals(solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]), 4)
        self.assertEquals(solution.findMinArrowShots(
            [[0, 9], [0, 6], [2, 9], [2, 8], [3, 9], [3, 8], [3, 9], [6, 8], [7, 12], [9, 10]]), 2)
