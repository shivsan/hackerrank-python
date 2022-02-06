from unittest import TestCase

from FruitBaskets import getMaxFruits, getMaxFruits_optimised


class Test(TestCase):
    def test_get_max_fruits(self):
        self.assertEquals(getMaxFruits([1, 2, 3, 2, 2]), 4)
        self.assertEquals(getMaxFruits([1, 2, 1]), 3)
        self.assertEquals(getMaxFruits([0, 1, 2, 2]), 3)

    def test_get_max_fruits_optimised(self):
        self.assertEquals(getMaxFruits_optimised([0, 0, 1, 1]), 4)
        self.assertEquals(getMaxFruits_optimised([1, 2, 3, 2, 2]), 4)
        self.assertEquals(getMaxFruits_optimised([1, 2, 1]), 3)
        self.assertEquals(getMaxFruits_optimised([0, 1, 2, 2]), 3)
        self.assertEquals(getMaxFruits_optimised([0, 1, 2]), 2)
