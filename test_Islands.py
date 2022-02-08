from unittest import TestCase

from Islands import Solution


class TestSolution(TestCase):
    def test_get_number_of_islands(self):
        solution = Solution()
        map = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]

        self.assertEquals(solution.getNumberOfIslands(map), 1)

        solution = Solution()
        map = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]

        self.assertEquals(solution.getNumberOfIslands(map), 3)
