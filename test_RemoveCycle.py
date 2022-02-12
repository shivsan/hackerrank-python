from unittest import TestCase

from RemoveCycle import Solution


class TestSolution(TestCase):
    def test_find_redundant_connection(self):
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        Output = [1, 4]

        self.assertEquals(Solution().findRedundantConnection(edges), Output)

        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        Output = [1, 4]

        self.assertEquals(Solution().findRedundantConnection(edges), Output)

        edges = [[2, 7], [7, 8], [3, 6], [2, 5], [6, 8], [4, 8], [2, 8], [1, 8], [7, 10], [3, 9]]
        Output = [2, 8]

        self.assertEquals(Solution().findRedundantConnection(edges), Output)
