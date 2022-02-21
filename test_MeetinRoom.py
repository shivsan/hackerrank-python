from unittest import TestCase

from MeetinRoom import Solution


class TestSolution(TestCase):
    def test_min_meeting_rooms(self):
        solution = Solution()

        self.assertEquals(solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]), 2)
        self.assertEquals(solution.minMeetingRooms([[7, 10], [2, 4]]), 1)

    def test_binary_search_greater_than_equal_to(self):
        solution = Solution()
        self.assertEquals(solution.binarySearchGreaterThan([0, 5, 15], 6), 2)
        self.assertEquals(solution.binarySearchGreaterThan([0, 5, 15], 15), 2)
        self.assertEquals(solution.binarySearchGreaterThan([0, 5, 15], 0), 0)
