from unittest import TestCase

from googleMaps import getShortestDistance, getPlace

class Test(TestCase):
    def test_get_shortest_distance(self):
        getShortestDistance()

    def test_When_no_path_exists_between_destination_and_source(self):
        self.fail()


class Test(TestCase):
    def test_get_place(self):
        getPlace()

    def test_When_no_results_for_place(self):
        self.fail()
