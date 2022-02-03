from unittest import TestCase

from FruitBaskets import getMaxFruits


class Test(TestCase):
    def test_get_max_fruits(self):
        self.assertEquals(getMaxFruits([1, 2, 3, 2, 2]), 4)
        self.assertEquals(getMaxFruits([1, 2, 1]), 3)
        self.assertEquals(getMaxFruits([0, 1, 2, 2]), 3)
