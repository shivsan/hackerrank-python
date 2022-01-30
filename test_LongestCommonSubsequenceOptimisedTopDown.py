from unittest import TestCase

import LongestCommonSubsequence


class Test(TestCase):
    def test_get_longest_common_subsequence_rec(self):
        self.assertEquals(LongestCommonSubsequence.getLongestCommonSubsequenceRecursiveStart("ahcead", "acaed"), "acad")

