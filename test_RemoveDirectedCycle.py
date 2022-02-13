from unittest import TestCase

from RemoveDirectedCycle import Solution


class TestSolution(TestCase):
    def test_find_redundant_directed_connection_normal(self):
        edges = [[1, 2], [1, 3], [2, 3]]
        Output = [2, 3]

        self.assertEquals(Solution().findRedundantDirectedConnection(edges), Output)

    def test_find_redundant_directed_connection_root_node(self):
        edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
        Output = [4, 1]

        self.assertEquals(Solution().findRedundantDirectedConnection(edges), Output)

    def test_find_redundant_directed_connection_hybrid(self):
        edges = [[2, 1], [3, 1], [4, 2], [1, 4]]
        Output = [2, 1]

        self.assertEquals(Solution().findRedundantDirectedConnection(edges), Output)
