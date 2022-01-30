from unittest import TestCase

import LengthOfLongestCommonSubsequenceOptimisedTopDown

class Test(TestCase):
    def test_get_length_longest_common_subsequence_recursive_optimised(self):
        self.assertEquals(LengthOfLongestCommonSubsequenceOptimisedTopDown.getLengthLongestCommonSubsequenceRecursiveOptimised("ahcead", "acaed"), 4)
