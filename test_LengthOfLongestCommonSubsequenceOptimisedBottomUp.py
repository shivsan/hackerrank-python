from unittest import TestCase

import LengthOfLongestCommonSubsequenceOptimisedBottomUp


class Test(TestCase):
    def test_get_length_longest_common_subsequence_recursive_optimised(self):
        self.assertEquals(LengthOfLongestCommonSubsequenceOptimisedBottomUp.getLengthLongestCommonSubsequenceRecursiveOptimised("ahcead", "acaed"), 4)
