from unittest import TestCase

from point_1.sorting.Methods import Sorters


class TestSorters(TestCase):
    def test_shaker_sort(self):
        ls = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
        print(Sorters.shaker_sort(ls))