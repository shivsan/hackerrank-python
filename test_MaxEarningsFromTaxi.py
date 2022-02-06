from unittest import TestCase

from MaxEarningsFromTaxi import getMaxEarningsFromTaxi


class Test(TestCase):
    def test_get_max_earnings_from_taxi_1(self):
        self.assertEquals(getMaxEarningsFromTaxi(5, [[2, 5, 4], [1, 5, 1]]), 7)

    def test_get_max_earnings_from_taxi_2(self):
        self.assertEquals(
            getMaxEarningsFromTaxi(20, [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]), 20)
